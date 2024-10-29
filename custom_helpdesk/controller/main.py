from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk

class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(['/helpdesk/create'], type='http', auth="public", website=True, csrf=False)
    def helpdesk_ticket_create(self, **kwargs):
        # Extraer el usuario autenticado y sus datos de res.partner
        user = request.env.user
        if user.partner_id:
            kwargs['sede'] = user.partner_id.sede
            kwargs['lugar'] = user.partner_id.lugar

        # Llamada al controlador original para crear el ticket
        return super(CustomWebsiteHelpdesk, self).helpdesk_ticket_create(**kwargs)



