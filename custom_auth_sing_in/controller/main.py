from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound


class AuthSignupHomeCustom(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        qcontext = super().get_auth_signup_qcontext()
        for field in ["estancia_id", "obra_id"]:
            value = http.request.params.get(field)
            if value:
                try:
                    qcontext[field] = int(value)
                except ValueError:
                    qcontext[field] = (
                        value  
                    )
        return qcontext

    def _prepare_signup_values(self, qcontext):
        # Llama al método original para obtener los valores básicos
        values = super()._prepare_signup_values(qcontext)

        def get_record_id(model, value):
            if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
                return int(value)
            record = request.env[model].sudo().search([('name', '=', value)], limit=1)
            return record.id if record else None

        if qcontext.get("estancia_id"):
            values["estancia_id"] = get_record_id("estancias.capitulo", qcontext["estancia_id"])
        if qcontext.get("obra_id"):
            values["obra_id"] = get_record_id("obra", qcontext["obra_id"])

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
