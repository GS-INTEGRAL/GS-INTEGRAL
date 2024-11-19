from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import NotFound
import logging

_logger = logging.getLogger(__name__)


class AuthSignupHomeCustom(AuthSignupHome):

    @http.route("/web/signup", type="http", auth="public", website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        _logger.info("Iniciando web_auth_signup personalizado")
        qcontext = self.get_auth_signup_qcontext()

        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_signup(qcontext)
                # Obtener el partner recién creado
                user = request.env['res.users'].sudo().search([('login', '=', qcontext.get('login'))])
                partner = user.partner_id

                # Actualizar los campos personalizados
                partner.sudo().write({
                    'obra_id': qcontext.get('obra_id'),
                    'obra_secundaria': qcontext.get('obra_secundaria'),
                    'estancia_id': qcontext.get('estancia_id'),
                })

                return self.web_login(*args, **kw)
            except Exception as e:
                qcontext['error'] = str(e)

        # Proporcionar opciones para los campos de selección
        qcontext.update({
            'obra_options': [
                ("lavaqua", "Lavaqua"),
                ("legal fincas", "Legal Fincas"),
                ("clientes varios", "Clientes Varios"),
                ("maristas", "Maristas"),
            ],
            'obra_secundaria_options': [
                ("fuensanta", "Fuensanta"),
                ("merced", "Merced"),
            ],
        })

        response = request.render('auth_signup.signup', qcontext)
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    def get_auth_signup_qcontext(self):
        qcontext = super(AuthSignupHomeCustom, self).get_auth_signup_qcontext()
        
        if request.httprequest.method == 'POST':
            qcontext.update({
                'obra_id': request.params.get('obra_id'),
                'obra_secundaria': request.params.get('obra_secundaria'),
                'estancia_id': request.params.get('estancia_id'),
            })
        
        return qcontext