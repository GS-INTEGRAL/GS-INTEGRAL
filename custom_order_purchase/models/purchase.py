from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    helpdesk_ticket_id = fields.Many2one(
        'helpdesk.ticket', 
        string='Ticket Relacionado',
        tracking=True
    )