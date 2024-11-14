from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
import logging

_logger = logging.getLogger(__name__)


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        "/website/helpdesk/form/",
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def website_form(self, **kwargs):
        user = request.env.user
        partner = user.partner_id if user.partner_id else None

        # Obtener la categoría desde los argumentos del formulario
        categoria = kwargs.get("categoria")
        
        # Asignar valores para obra y estancia si el partner está disponible
        if partner:
            kwargs["obra_id"] = partner.obra_id.display_name if partner.obra_id else ""
            kwargs["estancia_id"] = partner.estancia_id.display_name if partner.estancia_id else ""
        else:
            kwargs["obra_id"] = ""
            kwargs["estancia_id"] = ""
        
        # Preparar los valores para el ticket
        ticket_values = {
            "categoria": categoria,
            "partner_id": partner.id if partner else None,
            "obra_id": kwargs["obra_id"],
            "estancia_id": kwargs["estancia_id"],
        }
        
        # Crear el ticket en el modelo de helpdesk
        ticket = request.env["helpdesk.ticket"].sudo().create(ticket_values)

        # Renderizar la vista con los datos pasados
        return request.render(
            "helpdesk.helpdesk_ticket_view_form",
            {
                "partner": partner,
                "obra_id": kwargs["obra_id"],
                "estancia_id": kwargs["estancia_id"],
                "ticket": ticket,
            },
        )