from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request

class AuthSignupHomeInherit(AuthSignupHome):

    def do_signup(self, qcontext):
        # Llama al método original para manejar el proceso de registro
        super(AuthSignupHomeInherit, self).do_signup(qcontext)

        # Agrega los valores de sede y lugar al usuario recién creado
        if qcontext.get('sede') and qcontext.get('lugar'):
            user = request.env['res.users'].sudo().search([('login', '=', qcontext.get('login'))], limit=1)
            user.sede = qcontext.get('sede')
            user.lugar = qcontext.get('lugar')
