from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm

class CustomWebsiteForm(WebsiteForm):

    def _handle_website_form(self, model_name, **kwargs):
        # Ejecuta la lógica original del método padre
        result = super(CustomWebsiteForm, self)._handle_website_form(model_name, **kwargs)

        # Añadir lógica solo si es un ticket de soporte
        if model_name == 'helpdesk.ticket':
            partner_id = request.params.get('partner_id')
            partner = request.env['res.partner'].sudo().browse(partner_id)

            # Asignar los campos adicionales `sede` y `lugar` al ticket
            if partner:
                request.params['sede'] = partner.sede
                request.params['lugar'] = partner.lugar

        return result
