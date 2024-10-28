from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError

class AuthSignupHomeCustom(AuthSignupHome):

    def _prepare_signup_values(self, qcontext):
        # Llama al método original para obtener los valores básicos
        values = super()._prepare_signup_values(qcontext)

        # Agrega los campos adicionales al diccionario de valores
        values['lugar'] = qcontext.get('lugar')
        values['sede'] = qcontext.get('sede')

        return values
