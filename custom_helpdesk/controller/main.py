from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
from odoo.tools import html_sanitize
import logging

_logger = logging.getLogger(__name__)

class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        ["/custom_helpdesk/create"],
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def website_create(self, **kwargs):
        # Verificar si el usuario está autenticado
        if not request.env.user or request.env.user._is_public():
            return request.redirect("/web/login?redirect=/helpdesk")

        # Obtener datos del usuario
        user = request.env.user
        partner = user.partner_id if user.partner_id else None
        obra_id = partner.obra_id
        estancia_id = partner.estancia_id
        categoria = kwargs.get("categoria")

        # Limpiar descripción
        raw_description = kwargs.get("description", "")
        clean_description = html_sanitize(raw_description)

        # Crear ticket
        ticket_vals = {
            "name": "Ticket desde la Web",
            "partner_id": partner.id,
            "obra_id": obra_id,
            "estancia_id": estancia_id,
            "categoria": categoria,
            "description": clean_description,
        }

        ticket = request.env["helpdesk.ticket"].sudo().create(ticket_vals)

        # Redirigir al ticket creado
        return request.redirect(f"/helpdesk/ticket/{ticket.id}")