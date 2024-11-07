from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
import logging
from odoo.error import UserError

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
        prioridad = kwargs.get("prioridad")
        email = kwargs.get("partner_email")
        attachment = kwargs.get("Attachment")

        if not categoria or not prioridad:
            raise UserError("Faltan algunos datos requeridos para crear el ticket.")

        if partner:
            # Log para verificar que partner y sus campos están disponibles
            _logger.info(
                "Partner encontrado: %s, Sede: %s, Lugar: %s",
                partner.name,
                partner.sede,
                partner.lugar,
            )
            kwargs["sede"] = partner.sede
            kwargs["lugar"] = partner.lugar
            kwargs["email"] = partner.email or email
        else:
            _logger.warning("No se encontró el partner para el usuario: %s", user.login)
            kwargs["sede"] = ""
            kwargs["lugar"] = ""
            kwargs["email"] = email

        ticket_values = {
            "sede": kwargs["sede"],
            "lugar": kwargs["lugar"],
            "categoria": categoria,
            "prioridad": prioridad,
            "partner_id": partner.id if partner else None,
            "email": kwargs["email"],
            # "email_cc": kwargs["email"],
        }

        ticket = request.env["helpdesk.ticket"].sudo().create(ticket_values)

        # Agregar el archivo adjunto, si existe
        if attachment:
            attachment_data = (
                attachment.read() if hasattr(attachment, "read") else attachment
            )
            request.env["ir.attachment"].sudo().create(
                {
                    "name": attachment.filename,
                    "datas": attachment_data.encode("base64"),
                    "res_model": "helpdesk.ticket",
                    "res_id": ticket.id,
                }
            )

        # Renderizar la vista con los datos pasados
        return request.render(
            "website_helpdesk.team_form_1",
            {
                "partner": partner,
                "sede": kwargs.get("sede"),
                "lugar": kwargs.get("lugar"),
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
