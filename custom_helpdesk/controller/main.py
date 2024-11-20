from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
from odoo.tools import html_sanitize
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

        if partner:

            kwargs["obra_id"] = partner.obra_id
            kwargs["estancia_id"] = partner.estancia_id
        else:

            kwargs["obra_id"] = ""
            kwargs["estancia_id"] = ""

        # raw_description = kwargs.get("description", "")
        # clean_description = html_sanitize(raw_description)

        return request.render(
            "website_helpdesk.team_form_1",
            {
                "partner": partner,
                "obra_id": kwargs.get("obra_id"),
                "estancia_id": kwargs.get("estancia_id"),
            },
        )
