from odoo import http
from odoo.addons.website_helpdesk.controllers.main import WebsiteHelpdesk

class WebsiteHelpdeskExtended(WebsiteHelpdesk):

    @http.route()
    def submit_ticket(self, **kwargs):
        if kwargs.get('sede'):
            kwargs['description'] = f"Sede: {kwargs['sede']}\n\n{kwargs.get('description', '')}"
        return super(WebsiteHelpdeskExtended, self).submit_ticket(**kwargs)
