from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk

class CustomWebsiteHelpdesk(WebsiteHelpdesk):

        @http.route(['/helpdesk/create'], type='http', auth="public", website=True, csrf=False)
        def helpdesk_ticket_create(self, **kwargs):
            user = request.env.user
            partner = user.partner_id if user.partner_id else None  # Asegúrate de que el partner existe
            
            if partner:
                kwargs['sede'] = partner.sede
                kwargs['lugar'] = partner.lugar

            # Llamada al controlador original
            response = super(CustomWebsiteHelpdesk, self).helpdesk_ticket_create(**kwargs)
            response.qcontext.update({
                'partner': partner,  # Agregar el objeto partner
                'sede': kwargs.get('sede'),
                'lugar': kwargs.get('lugar')
            })
            return response



