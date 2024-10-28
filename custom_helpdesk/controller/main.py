from odoo import http
from odoo.http import request

class WebsiteHelpdesk(http.Controller):
    
    @http.route('/helpdesk/ticket/submit', type='http', auth='user', website=True)
    def helpdesk_ticket_submit(self, **kwargs):
        partner = request.env.user.partner_id
        values = {
            'partner': partner,
            'sede': partner.sede,
            'lugar': partner.lugar,
        }
        return request.render('website_helpdesk.ticket_form_template', values)

    @http.route('/helpdesk/ticket/create', type='http', auth='user', website=True)
    def helpdesk_ticket_create(self, **post):
        partner = request.env.user.partner_id
        ticket_vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'sede': post.get('sede') or partner.sede,
            'lugar': post.get('lugar') or partner.lugar,
            # otros campos de ticket...
        }
        ticket = request.env['helpdesk.ticket'].sudo().create(ticket_vals)
        return request.redirect('/helpdesk/ticket/thanks')
