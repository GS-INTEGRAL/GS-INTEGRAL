from odoo import models, fields, api

class PurchaseOrderConfirmationWizard(models.TransientModel):
    _name = 'purchase.order.confirmation.wizard'
    _description = 'Purchase Order Confirmation Wizard'

    ticket_id = fields.Many2one(
        'helpdesk.ticket', 
        string='Ticket Relacionado',
        required=True
    )
    purchase_order_id = fields.Many2one(
        'purchase.order', 
        string='Orden de Compra',
        required=True
    )
    partner_id = fields.Many2one(
        'res.partner', 
        string='Proveedor',
        required=True
    )

    def confirm_purchase_order(self):
        # Aquí puedes añadir lógica adicional de confirmación
        self.purchase_order_id.button_confirm()
        return {'type': 'ir.actions.act_window_close'}

    def cancel_purchase_order(self):
        # Eliminar la orden de compra si se cancela
        self.purchase_order_id.unlink()
        return {'type': 'ir.actions.act_window_close'}