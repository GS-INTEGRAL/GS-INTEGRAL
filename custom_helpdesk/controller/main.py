from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
import logging

_logger = logging.getLogger(__name__)


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        ["/helpdesk/create"],
        type="http",
        auth="user",
        website=True,
        csrf=False,
    )
    def website_create(self, **kwargs):
        if request.env.user.has_group("base.group_public"):
   
            return request.redirect("/web/login?redirect=/helpdesk")
        
        user = request.env.user
        partner = user.partner_id if user.partner_id else None
                  
        obra_id = partner.obra_id
        estancia_id = partner.estancia_id
        categoria = kwargs.get("categoria")
                
        ticket_vals = {
            "name": "Ticket desde la Web",
            "partner_id": partner.id,
            "obra_id": obra_id,
            "estancia_id": estancia_id,
            "categoria": categoria,
        }

        ticket = request.env["helpdesk.ticket"].sudo().create(ticket_vals)

        # Redirigir al usuario a la página de confirmación o al ticket creado
        return request.redirect(f"/helpdesk/ticket/{ticket.id}")
