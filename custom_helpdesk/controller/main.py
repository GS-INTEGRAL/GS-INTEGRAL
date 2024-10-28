from odoo import http
from odoo.addons.website_helpdesk.controllers.main import WebsiteForm

class CustomWebsiteForm(WebsiteForm):

    def _handle_website_form(self, model_name, **kwargs):
        # Recuperar los parámetros sede y lugar
        sede = request.params.get('sede')
        lugar = request.params.get('lugar')
        email = request.params.get('partner_email')

        if email:
            if request.env.user.email == email:
                partner = request.env.user.partner_id
            else:
                partner = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)
            
            # Si no existe el partner, crearlo con los campos adicionales
            if not partner:
                partner = request.env['res.partner'].sudo().create({
                    'email': email,
                    'name': request.params.get('partner_name', False),
                    'lang': request.lang.code,
                    'sede': sede,
                    'lugar': lugar,
                })
            else:
                # Si el partner existe, actualizar los campos sede y lugar
                partner.sudo().write({
                    'sede': sede,
                    'lugar': lugar,
                })

            request.params['partner_id'] = partner.id

        # Llamar al método original
        return super(CustomWebsiteForm, self)._handle_website_form(model_name, **kwargs)
