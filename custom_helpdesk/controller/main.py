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
        prioridad = kwargs.get("prioridad")
        email = kwargs.get("partner_email")

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
            kwargs["email"] = partner.email
        else:
            _logger.warning("No se encontró el partner para el usuario: %s", user.login)
            kwargs["sede"] = ""
            kwargs["lugar"] = ""
            kwargs["email"] = ""

        _logger.info(
            "Datos enviados a la vista - Sede: %s, Lugar: %s",
            kwargs.get("sede"),
            kwargs.get("lugar"),
        )

        ticket = (
            request.env["helpdesk.ticket"]
            .sudo()
            .create(
                {
                    "sede": kwargs["sede"],
                    "lugar": kwargs["lugar"],
                    "categoria": categoria,
                    "prioridad": prioridad,
                    "partner_id": partner.id if partner else None,
                    "email": kwargs["email"],
                }
            )
        )

        return request.render(
            "website_helpdesk.team_form_1",
            {
                "partner": partner,
                "sede": kwargs.get("sede"),
                "lugar": kwargs.get("lugar"),
                "ticket": ticket,
            },
        )
