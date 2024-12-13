from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
from odoo.tools import html_sanitize

from werkzeug.exceptions import NotFound
import logging

_logger = logging.getLogger(__name__)


def ensure_authenticated_user():
    if not request.env.user or request.env.user._is_public():
        return request.redirect("/web/login?redirect=/helpdesk")
    return None


class CustomWebsiteHelpdeskTeams(http.Controller):

    @http.route(
        ["/helpdesk", '/helpdesk/<model("helpdesk.team"):team>'],
        type="http",
        auth="public",
        website=True,
    )
    def website_helpdesk_teams(self, team=None, **kwargs):
        if request.env.user._is_public():
            return request.redirect("/web/login?redirect=/helpdesk")

        
        teams_domain = [("use_website_helpdesk_form", "=", True)]        
        teams = request.env["helpdesk.team"].search(teams_domain, order="id asc")
        if not teams:
            raise NotFound()

        # Renderizamos la vista del equipo de helpdesk
        result = {
            "team": team or teams[0],
            "multiple_teams": len(teams) > 1,
            "main_object": team or teams[0],
        }
        return request.render("website_helpdesk.team", result)


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        ["/custom_helpdesk/create"],
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def website_create(self, **kwargs):
        # Verificar autenticación
        redirection = ensure_authenticated_user()
        if redirection:
            return redirection

        #  # Validar que el usuario tiene asignada una compañía
        if not request.env.partner_id.parent_id:
            return request.render("website_helpdesk.not_authorized", {
                'error_message': 'No tiene asignada una compañía. Por favor, póngase en contacto con el administrador.'
            })


        return request.redirect("/helpdesk")

    @http.route(
        ["/my/ticket"],
        type="http",
        auth="user",
        website=True,
    )
    def redirect_my_ticket(self, **kwargs):
        return request.redirect("/helpdesk")
