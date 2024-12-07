from odoo import _, models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order'

    helpdesk_ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket Relacionado')
    helpdesk_user_id = fields.Many2one('res.users', string='Empleado Asignado', related='helpdesk_ticket_id.user_id', store=True, readonly=True)