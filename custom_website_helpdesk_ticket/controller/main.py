# controllers/custom_helpdesk_controller.py
from odoo import http
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound


class CustomWebsiteHelpdesk(http.Controller):

    @http.route(
        ["/helpdesk", '/helpdesk/<model("helpdesk.team"):team>'],
        type="http",
        auth="user",
        website=True,
    )
    def website_helpdesk_teams(self, team=None, **kwargs):
        # Verificar si el usuario está autenticado
        if request.env.user._is_public():
            # Redirigir al login si no está autenticado
            return request.redirect("/web/login?redirect=/helpdesk")

        # Aquí continuamos con la lógica para mostrar los equipos del helpdesk
        teams_domain = [("use_website_helpdesk_form", "=", True)]
        if not request.env.user.has_group("helpdesk.group_helpdesk_manager"):
            if team and not team.is_published:
                raise NotFound()
            teams_domain.append(("website_published", "=", True))

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
