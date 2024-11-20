from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome as BaseAuthSignupHome
from odoo.http import request


class AuthSignupHome(http.Controller):

    @http.route("/web/signup", type="http", auth="public", website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()

        if "error" not in qcontext and request.httprequest.method == "POST":
            try:
                self.do_signup(qcontext)
                user = (
                    request.env["res.users"]
                    .sudo()
                    .search([("login", "=", qcontext.get("login"))])
                )
                if user:
                    partner = user.partner_id
                    partner.write(
                        {
                            "obra_id": qcontext.get("obra_id"),
                            "obra_secundaria": qcontext.get("obra_secundaria"),
                            "estancia_id": qcontext.get("estancia_id"),
                        }
                    )
                return self.web_login(*args, **kw)
            except Exception as e:
                qcontext["error"] = str(e)

        response = request.render("auth_signup.signup", qcontext)
        response.headers["X-Frame-Options"] = "DENY"
        return response

    def get_auth_signup_qcontext(self):
        qcontext = super(AuthSignupHome, self).get_auth_signup_qcontext()
        qcontext.update(
            {
                "obra_id": request.params.get("obra_id"),
                "obra_secundaria": request.params.get("obra_secundaria"),
                "estancia_id": request.params.get("estancia_id"),
            }
        )
        return qcontext

    def do_signup(self, qcontext):
        values = {
            key: qcontext.get(key)
            for key in (
                "login",
                "name",
                "password",
                "obra_id",
                "obra_secundaria",
                "estancia_id",
            )
        }
        request.env["res.users"].sudo().signup(values, qcontext.get("token"))
