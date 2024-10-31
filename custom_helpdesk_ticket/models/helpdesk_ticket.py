from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    sede = fields.Char(string="Sede", related="partner_id.user_ids.sede", store=True)
    lugar = fields.Char(string="Lugar", related="partner_id.user_ids.lugar", store=True)
