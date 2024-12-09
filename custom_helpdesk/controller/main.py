from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
from odoo.tools import html_sanitize

from werkzeug.exceptions import NotFound
import logging

_logger = logging.getLogger(__name__)


def ensure_authenticated_user():
    if not request.env.user or request.env.user._is_public():
        return request.redirect("/web/login?redirect=/helpdesk")
    return None


class CustomWebsiteHelpdeskTeams(http.Controller):

    @http.route(
        ["/helpdesk", '/helpdesk/<model("helpdesk.team"):team>'],
        type="http",
        auth="user",
        website=True,
    )
    def website_helpdesk_teams(self, team=None, **kwargs):
        if request.env.user._is_public():

            return request.redirect("/web/login?redirect=/helpdesk")

        teams_domain = [("use_website_helpdesk_form", "=", True)]
        if not request.env.user.has_group("helpdesk.group_helpdesk_manager"):
            if team and not team.is_published:
                raise NotFound()
            teams_domain.append(("website_published", "=", True))

        teams = request.env["helpdesk.team"].search(teams_domain, order="id asc")
        if not teams:
            raise NotFound()

        # Renderizamos la vista del equipo de helpdesk
        result = {
            "team": team or teams[0],
            "multiple_teams": len(teams) > 1,
            "main_object": team or teams[0],
        }
        return request.render("website_helpdesk.team", result)


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        ["/custom_helpdesk/create"],
        type="http",
        auth="user",
        website=True,
        csrf=False,
    )
    def website_create(self, **kwargs):
        # Verificar autenticación
        redirection = ensure_authenticated_user()
        if redirection:
            return redirection

        # Obtener datos del usuario
        user = request.env.user
        partner = user.partner_id if user.partner_id else None

        # # Validar que el partner tiene permisos necesarios
        # obra_id = kwargs.get("obra_secundaria")
        # estancia_id = kwargs.get("estancia_id")
        # categoria = kwargs.get("categoria", "").strip()
        # Convertir campos Many2one 
        try:
            obra_secundaria = int(kwargs.get("obra_secundaria", 0))
            estancia_id = int(kwargs.get("estancia_id", 0))
        except (ValueError, TypeError):
            return request.redirect("/helpdesk?error=invalid_selection")

        # Validar campos personalizados
        if not obra_secundaria or not estancia_id:
            return request.redirect("/helpdesk?error=missing_required_fields")
       
        # Preparar valores para el ticket
        ticket_vals = {
            "name": kwargs.get("subject", "Ticket desde la Web"),
            "partner_id": partner.id if partner else None,
            "description": html_sanitize(kwargs.get("description", "")),
            "obra_secundaria": obra_secundaria,
            "estancia_id": estancia_id,
            "categoria": kwargs.get("categoria", "").strip(),
        }

        try:
            # Crear ticket
            ticket = request.env["helpdesk.ticket"].sudo().create(ticket_vals)

            # Manejar archivos adjuntos (opcional)
            if kwargs.get('attachment'):
                Attachment = request.env['ir.attachment']
                for attachment in kwargs.get('attachment'):
                    Attachment.sudo().create({
                        'name': attachment.filename,
                        'datas': base64.b64encode(attachment.read()),
                        'res_model': 'helpdesk.ticket',
                        'res_id': ticket.id,
                    })

        except Exception as e:
            _logger.error("Error creando el ticket: %s", str(e))
            return request.redirect("/helpdesk?error=creation_failed")

        return request.redirect(f"/helpdesk/ticket/{ticket.id}")