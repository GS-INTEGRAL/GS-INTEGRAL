from odoo import http
from odoo.http import request
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk
from odoo.tools import html_sanitize

from werkzeug.exceptions import NotFound
import logging

_logger = logging.getLogger(__name__)


def ensure_authenticated_user():
    _logger.info("Verificando autenticación para el usuario %s", request.env.user.name)
    if not request.env.user or request.env.user._is_public():
        _logger.info("Redirigiendo al login")
        return request.redirect("/web/login?redirect=/helpdesk")
    return None


class CustomWebsiteHelpdesk(WebsiteHelpdesk):

    @http.route(
        ["/helpdesk/create"],
        type="http",
        auth="user",
        website=True,
        csrf=False,
    )
    def website_create(self, **kwargs):
        _logger.info("CustomWebsiteHelpdesk create method called")
        # Verificar autenticación
        redirection = ensure_authenticated_user()
        if redirection:
            _logger.info("Redirigiendo al login")
            return redirection

        # Obtener datos del usuario
        user = request.env.partner_id
        if not user.company_id:
            return request.redirect("/helpdesk?error=no_company")

        # Determinar si es Maristas
        is_maristas = user.company_id.name == "Maristas"

        # Validar campos según la compañía
        if is_maristas:
            required_fields = ["obras", "estanciasid"]
        else:
            required_fields = ["obra_secundaria", "estancia_id"]

        missing_fields = [field for field in required_fields if not kwargs.get(field)]
        if missing_fields:
            _logger.warning("Campos faltantes al crear el ticket: %s", missing_fields)
            return request.redirect("/custom_helpdesk/create?error=missing_fields")

        # Preparar valores para el ticket
        ticket_vals = {
            "name": kwargs.get("subject", "Ticket desde la Web"),
            "partner_id": user.partner_id.id if user.partner_id else None,
            "description": html_sanitize(kwargs.get("description", "")),
            "obra_secundaria": kwargs.get("obra_secundaria"),
            "estancia_id": kwargs.get("estancia_id"),
            "categoria": kwargs.get("categoria").strip(),
            "obras": kwargs.get("obras"),
            "estanciasid": kwargs.get("estanciasid"),
        }

        # Crear ticket
        try:
            # Crear el ticket
            ticket = request.env["helpdesk.ticket"].sudo().create(ticket_vals)
        except Exception as e:
            _logger.error("Error creando el ticket: %s", str(e))
            return request.redirect("/helpdesk?error=creation_failed")

        # Redirigir al ticket creado
        return request.redirect(f"/helpdesk/ticket/{ticket.id}")


# class CustomWebsiteHelpdeskTeamsStaging(http.Controller):

#     def __init__(self):
#         super().__init__()
#         _logger.info("CustomWebsiteHelpdeskTeams controller loaded")

#     @http.route(
#         ["/helpdesk_stag", '/helpdesk_stag/<model("helpdesk.team"):team>'],
#         type="http",
#         auth="user",
#         website=True,
#     )
#     def website_helpdesk_teams(self, team=None, **kwargs):
#         _logger.info("website_helpdesk_teams method called")

#         if request.env.user._is_public():
#             return request.redirect("/web/login?redirect=/helpdesk")

#         if not request.env.partner_id.company_id:
#             return request.redirect("/helpdesk?error=no_company")

#         teams_domain = [("use_website_helpdesk_form", "=", True)]

#         teams = request.env["helpdesk.team"].search(teams_domain, order="id asc")

#         if not teams:
#             raise NotFound()

#         # Renderizamos la vista del equipo de helpdesk
#         result = {
#             "team": team or teams[0],
#             "multiple_teams": len(teams) > 1,
#             "main_object": team or teams[0],
#         }
#         return request.render("website_helpdesk.team", result)
