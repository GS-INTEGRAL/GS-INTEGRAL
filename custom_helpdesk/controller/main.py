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
    def website_create(self, **kwargs):
        user = request.env.user
        partner = user.partner_id if user.partner_id else None

        if partner:
            obra_id = partner.obra_id.display_name if partner.obra_id else ""
            estancia_id = partner.estancia_id.display_name if partner.estancia_id else ""
        else:
            obra_id = ""
            estancia_id = ""

        return request.render(
            "website_helpdesk.team_form_1",
            {
                "partner": partner,
                "obra_id": obra_id,
                "estancia_id": estancia_id,
            },
        )