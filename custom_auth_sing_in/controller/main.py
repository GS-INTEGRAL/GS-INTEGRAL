from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound


class AuthSignupHomeCustom(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        # Llama al método original para obtener el contexto
        qcontext = super().get_auth_signup_qcontext()

        # Agrega los campos adicionales al contexto si están en request.params
        qcontext["estancia_id"] = http.request.params.get("estancia_id") or None
        qcontext["obra_id"] = http.request.params.get("obra_id") or None

        if qcontext["estancia_id"]:
            qcontext["estancia_id"] = int(qcontext["estancia_id"])
        if qcontext["obra_id"]:
            qcontext["obra_id"] = int(qcontext["obra_id"])

        return qcontext

    def _prepare_signup_values(self, qcontext):
        # Llama al método original para obtener los valores básicos
        values = super()._prepare_signup_values(qcontext)

        # Extrae y agrega los campos adicionales al diccionario de valores
        if qcontext.get("estancia_id"):
            if qcontext["estancia_id"].isdigit():
                qcontext["estancia_id"] = int(qcontext["estancia_id"])
            else:
                
                estancia = self.env["estancias.capitulo"].search(
                    [("name", "=", qcontext["estancia_id"])], limit=1
                )
                qcontext["estancia_id"] = estancia.id if estancia else None
                
        if qcontext.get("obra_id"):
            if qcontext["obra_id"].isdigit():
                qcontext["obra_id"] = int(qcontext["obra_id"])
            else:

                obra = self.env["obra"].search(
                    [("name", "=", qcontext["obra_id"])], limit=1
                )
                qcontext["obra_id"] = obra.id if obra else None

        return values


class WebsiteHelpdesk(http.Controller):

    @http.route(
        # ["/helpdesk", '/helpdesk/<model("helpdesk.team"):team>'],
        ["/helpdesk"],
        type="http",
        auth="user",
        website=True,
    )
    def website_helpdesk(self, **kwargs):
        if request.env.user._is_public():

            return request.redirect("/web/login?redirect=/helpdesk")

        user = request.env.user
        # Asignamos los valores de obra_id y estancia_id si están presentes en el usuario
        obra_id = user.partner_id.obra_id.id if user.partner_id.obra_id else None
        estancia_id = (
            user.partner_id.estancia_id.id if user.partner_id.estancia_id else None
        )

        # Ahora podemos pasar estos valores al formulario del ticket
        return request.render(
            "website_helpdesk.ticket_form",
            {
                "obra_id": obra_id,
                "estancia_id": estancia_id,
            },
        )

    # def website_helpdesk_teams(self, team=None, **kwargs):
    #     # Verificar si el usuario está autenticado
    #     if request.env.user._is_public():
    #         # Redirigir al login si no está autenticado
    #         return request.redirect("/web/login?redirect=/helpdesk")

    #     # Aquí continuamos con la lógica para mostrar los equipos del helpdesk
    #     teams_domain = [("use_website_helpdesk_form", "=", True)]
    #     if not request.env.user.has_group("helpdesk.group_helpdesk_manager"):
    #         if team and not team.is_published:
    #             raise NotFound()
    #         teams_domain.append(("website_published", "=", True))

    #     teams = request.env["helpdesk.team"].search(teams_domain, order="id asc")
    #     if not teams:
    #         raise NotFound()

    #     # Renderizamos la vista del equipo de helpdesk
    #     result = {
    #         "team": team or teams[0],
    #         "multiple_teams": len(teams) > 1,
    #         "main_object": team or teams[0],
    #     }
    #     return request.render("website_helpdesk.team", result)
