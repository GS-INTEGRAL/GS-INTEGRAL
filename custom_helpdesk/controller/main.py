from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
import logging

_logger = logging.getLogger(__name__)


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        ["/helpdesk/create"],
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def helpdesk_ticket_create(self, **kwargs):
        user = request.env.user
        partner = user.partner_id if user.partner_id else None

        categoria = kwargs.get("categoria")
        email = kwargs.get("partner_email")
        sede_imagen = kwargs.get("sede_imagen")
        lugar_incidencia_imagen = kwargs.get("lugar_incidencia_imagen")

        if partner:

            kwargs["sede"] = partner.sede
            kwargs["lugar"] = partner.lugar
            kwargs["email"] = partner.email or email
        else:
            kwargs["sede"] = ""
            kwargs["lugar"] = ""
            kwargs["email"] = email

        ticket_values = {
            "sede": kwargs["sede"],
            "lugar": kwargs["lugar"],
            "categoria": categoria,
            "partner_id": partner.id if partner else None,
            "email": kwargs["email"],
            "email_cc": kwargs["email"],
        }

        # Añadir los archivos a los valores del ticket
        if sede_imagen and hasattr(sede_imagen, 'read'):
            ticket_values["sede_imagen"] = sede_imagen.read()
        if lugar_incidencia_imagen and hasattr(lugar_incidencia_imagen, 'read'):
            ticket_values["lugar_incidencia_imagen"] = lugar_incidencia_imagen.read()

        ticket = request.env["helpdesk.ticket"].sudo().create(ticket_values)

        # Renderizar la vista con los datos pasados
        return request.render(
            "website_helpdesk.team_form_1",
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
