from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk

class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(['/helpdesk/create'], type='http', auth="public", website=True, csrf=False)
    def helpdesk_ticket_create(self, **kwargs):
        # Obtenemos el usuario autenticado y sus datos de `res.partner`
        user = request.env.user
        if user.partner_id:
            # Pasamos los valores de `sede` y `lugar` desde el perfil del usuario al contexto
            kwargs['sede'] = user.partner_id.sede
            kwargs['lugar'] = user.partner_id.lugar

        # Llamada al controlador original para renderizar el formulario
        response = super(CustomWebsiteHelpdesk, self).helpdesk_ticket_create(**kwargs)
        response.qcontext.update({
            'sede': kwargs.get('sede'),
            'lugar': kwargs.get('lugar')
        })
        return response


