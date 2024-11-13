from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound


class AuthSignupHomeCustom(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        # Llama al método original para obtener el contexto
        qcontext = super().get_auth_signup_qcontext()

        # Agrega los campos adicionales al contexto si están en request.params
        qcontext["estancia_id"] = http.request.params.get("estancia_id")
        qcontext["obra_id"] = http.request.params.get("obra_id")

        return qcontext

    def _prepare_signup_values(self, qcontext):
        # Llama al método original para obtener los valores básicos
        values = super()._prepare_signup_values(qcontext)

        # Extrae y agrega los campos adicionales al diccionario de valores
        values["estancia_id"] = qcontext.get("estancia_id")
        values["obra_id"] = qcontext.get("obra_id")

        return values

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
