from odoo.addons.website_helpdesk.controllers.main import WebsiteForm

class WebsiteFormExtended(WebsiteForm):

    def _handle_website_form(self, model_name, **kwargs):
        if model_name == 'helpdesk.ticket':
            sede = kwargs.get('sede')
            if sede:
                kwargs['description'] = f"Sede: {sede}\n\n{kwargs.get('description', '')}"
        
        return super(WebsiteFormExtended, self)._handle_website_form(model_name, **kwargs)
