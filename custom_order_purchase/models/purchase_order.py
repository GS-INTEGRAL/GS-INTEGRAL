from odoo import models, fields


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    ticket_id = fields.Many2one("helpdesk.ticket", string="Ticket relacionado")

    def action_create_purchase_order(self):
        purchase_order = self.env['purchase.order'].create({
            'partner_id': self.partner_id.id,
            'order_line': [(0, 0, {
                'product_id': line.product_id.id,
                'product_qty': line.product_qty,
                'price_unit': line.price_unit,
                'taxes_id': [(6, 0, line.taxes_id.ids)],
            }) for line in self.purchase_order_ids],
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'res_id': purchase_order.id,
        }
