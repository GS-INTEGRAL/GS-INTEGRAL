from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request


class CustomAuthSignupHome(AuthSignupHome):

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
        qcontext = super(CustomAuthSignupHome, self).get_auth_signup_qcontext()
        qcontext.update(
            {
                "obra_id": request.params.get("obra_id"),
                "obra_secundaria": request.params.get("obra_secundaria"),
                "estancia_id": request.params.get("estancia_id"),
            }
        )
        return qcontext

    def do_signup(self, qcontext):
        values = self._prepare_signup_values(qcontext)
        
        Partner = request.env['res.partner'].sudo()
        partner = Partner.create({
            'name': values.get('name'),
            'email': values.get('login'),  
            'obra_id': values.get('obra_id'),
            'obra_secundaria': values.get('obra_secundaria'),
            'estancia_id': values.get('estancia_id'),
        })

        portal_group = request.env.ref('base.group_portal')
        User = request.env['res.users'].sudo()
        user = User.create({
            'partner_id': partner.id,
            'login': values.get('login'),
            'password': values.get('password'),
            'name': values.get('name'),
            'groups_id': [(6, 0, [portal_group.id])],
            })

        template = request.env.ref('custom_auth_sing_in.email_template_welcome', raise_if_not_found=False)
        if partner and template:
            template.sudo().with_context(lang=partner.lang).send_mail(partner.id, force_send=True)

        request.env.cr.commit()

        request.session.authenticate(request.session.db, user.login, values.get('password'))
        
        return request.redirect('/web/login')
    
    def _prepare_signup_values(self, qcontext):
        values = super()._prepare_signup_values(qcontext)
        values.update({
            'obra_id': qcontext.get('obra_id'),
            'obra_secundaria': qcontext.get('obra_secundaria'),
            'estancia_id': qcontext.get('estancia_id'),
        })
        return values