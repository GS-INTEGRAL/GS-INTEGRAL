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

        # Validar que el partner tiene permisos necesarios
        obra_id = kwargs.get("obra_secundaria")
        estancia_id = kwargs.get("estancia_id")
        categoria = kwargs.get("categoria", "").strip()

       
        # Limpiar descripción
        raw_description = kwargs.get("description", "")
        clean_description = html_sanitize(raw_description)

        if not obra_id or not estancia_id:
            # Retorna un error si no se seleccionaron valores válidos
            return request.redirect("/helpdesk?error=missing_required_fields")
        
        # Crear ticket
        ticket_vals = {
            "name": kwargs.get("subject", "Ticket desde la Web"),
            "partner_id": partner.id if partner else None,
            "obra_secundaria": int(obra_id),  # Convertimos a int porque viene como string del formulario
            "estancia_id": int(estancia_id),
            "categoria": categoria,
            "description": clean_description,
        }

        try:
            ticket = request.env["helpdesk.ticket"].sudo().create(ticket_vals)
        except Exception as e:
            _logger.error("Error creando el ticket: %s", str(e))
            return request.redirect("/helpdesk?error=creation_failed")

        return request.redirect(f"/helpdesk/ticket/{ticket.id}")

    @http.route(
            ["/custom_helpdesk/form"],
            type="http",
            auth="user",
            website=True,
        )
    def custom_helpdesk_form(self, **kwargs):
        # Verificar autenticación
        redirection = ensure_authenticated_user()
        if redirection:
            return redirection
       
        # Obtener datos para poblar el formulario
        obras = request.env["res.partner.obra_secundaria"].sudo().search([])
        estancias = request.env["res.partner.estancia_id"].sudo().search([])

        # Renderizar el formulario con opciones dinámicas
        return request.render("custom_helpdesk.template_helpdesk_form", {
            "obras": obras,
            "estancias": estancias,
        })
    
    @http.route(['/custom_helpdesk/create_obra'], type='json', auth="user", website=True)
    def create_obra(self, name):
        obra = request.env['res.partner.obra_secundaria'].sudo().create({'name': name})
        return {'id': obra.id, 'name': obra.name}

    @http.route(['/custom_helpdesk/create_estancia'], type='json', auth="user", website=True)
    def create_estancia(self, name):
        estancia = request.env['res.partner.estancia_id'].sudo().create({'name': name})
        return {'id': estancia.id, 'name': estancia.name}