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
        partner = (
            user.partner_id if user.partner_id else None
        )  # Asegúrate de que el partner existe

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
        else:
            _logger.warning(
                "No se encontró el partner para el usuario: %s", user.login
            )
            kwargs["sede"] = ""
            kwargs["lugar"] = ""

        _logger.info(
            "Datos enviados a la vista - Sede: %s, Lugar: %s",
            kwargs.get("sede"),
            kwargs.get("lugar"),
        )

        return request.render(
            "website_helpdesk.team_form_1",
            {
                "partner": partner,
                "sede": kwargs.get("sede"),
                "lugar": kwargs.get("lugar"),
            },
        )
