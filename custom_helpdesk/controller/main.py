from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class AuthSignupHomeCustom(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        # Llama al método original para obtener el contexto
        qcontext = super().get_auth_signup_qcontext()

        # Agrega los campos adicionales al contexto si están en request.params
        qcontext['lugar'] = http.request.params.get('lugar')
        qcontext['sede'] = http.request.params.get('sede')

        return qcontext

    def _prepare_signup_values(self, qcontext):
        # Llama al método original para obtener los valores básicos
        values = super()._prepare_signup_values(qcontext)

        # Extrae y agrega los campos adicionales al diccionario de valores
        values['lugar'] = qcontext.get('lugar')
        values['sede'] = qcontext.get('sede')

        return values


