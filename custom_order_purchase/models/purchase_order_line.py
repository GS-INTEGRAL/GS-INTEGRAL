from odoo import _, models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    helpdesk_user_id = fields.Many2one('res.users', string='Empleado Asignado', related='order_id.helpdesk_ticket_id.user_id', store=True, readonly=True)
