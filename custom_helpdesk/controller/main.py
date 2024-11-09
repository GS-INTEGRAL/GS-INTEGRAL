from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
import logging

_logger = logging.getLogger(__name__)


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        "/website/form/",
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def website_form(self, **kwargs):
        user = request.env.user
        partner = user.partner_id if user.partner_id else None

        categoria = kwargs.get("categoria")
        partner_email = kwargs.get("partner_email")
        _logger.info("Email recibido en controlador: %s", partner_email)
        sede_imagen = kwargs.get("sede_imagen")
        lugar_incidencia_imagen = kwargs.get("lugar_incidencia_imagen")

        _logger.info(
            "Valores recibidos: categoria=%s, email=%s, sede_imagen=%s, lugar_incidencia_imagen=%s",
            categoria,
            partner_email,
            sede_imagen,
            lugar_incidencia_imagen,
        )

        if partner:

            kwargs["sede"] = partner.sede
            kwargs["lugar"] = partner.lugar
            kwargs["email"] = partner.email or partner_email
        else:
            kwargs["sede"] = ""
            kwargs["lugar"] = ""
            kwargs["email"] = partner_email

        _logger.info(
            "Valores de sede y lugar asignados: sede=%s, lugar=%s, email=%s",
            kwargs["sede"],
            kwargs["lugar"],
            kwargs["email"],
        )

        ticket_values = {
            "sede": kwargs["sede"],
            "lugar": kwargs["lugar"],
            "categoria": categoria,
            "partner_id": partner.id if partner else None,
            "email": kwargs["partner_email"],
            "email_cc": kwargs["partner_email"],
        }

        # Añadir los archivos a los valores del ticket
        if sede_imagen and hasattr(sede_imagen, "read"):
            ticket_values["sede_imagen"] = sede_imagen.read()
            _logger.info("Imagen de la sede cargada correctamente.")
        else:
            _logger.warning("No se encontró imagen para la sede.")

        if lugar_incidencia_imagen and hasattr(lugar_incidencia_imagen, "read"):
            ticket_values["lugar_incidencia_imagen"] = lugar_incidencia_imagen.read()
            _logger.info("Imagen del lugar de incidencia cargada correctamente.")
        else:
            _logger.warning("No se encontró imagen para el lugar de incidencia.")

        _logger.info("Datos del ticket antes de crear: %s", ticket_values)

        ticket = request.env["helpdesk.ticket"].sudo().create(ticket_values)

        # Renderizar la vista con los datos pasados
        return request.render(
            "helpdesk.helpdesk_ticket_view_form",
            {
                "partner": partner,
                "sede": kwargs.get("sede"),
                "lugar": kwargs.get("lugar"),
                "email_cc": kwargs.get("email"),
                "ticket": ticket,
            },
        )

        # _logger.info(
        #     "Datos enviados a la vista - Sede: %s, Lugar: %s",
        #     kwargs.get("sede"),
        #     kwargs.get("lugar"),
        # )

        # ticket = (
        #     request.env["helpdesk.ticket"]
        #     .sudo()
        #     .create(
        #         {
        #             "sede": kwargs["sede"],
        #             "lugar": kwargs["lugar"],
        #             "categoria": categoria,
        #             "prioridad": prioridad,
        #             "partner_id": partner.id if partner else None,
        #             "email": kwargs["email"],
        #         }
        #     )
        # )

        # return request.render(
        #     "website_helpdesk.team_form_1",
        #     {
        #         "partner": partner,
        #         "sede": kwargs.get("sede"),
        #         "lugar": kwargs.get("lugar"),
        #         "ticket": ticket,
        #     },
        # )
