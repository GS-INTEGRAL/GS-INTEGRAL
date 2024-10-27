from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

class CustomWebsiteHelpdesk(http.Controller):

    @http.route(['/helpdesk/create_ticket'], type='http', auth="user", website=True)
    def custom_helpdesk_create_ticket(self, **kwargs):
        # Asegurar autenticación
        if request.env.user._is_public():
            return request.redirect('/web/login?redirect=/helpdesk/create_ticket')

        # Lógica para mostrar el formulario de creación de incidencia o procesar su envío
        return request.render("website_helpdesk.create_ticket", {})

    
   
        