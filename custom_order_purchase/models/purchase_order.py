from odoo import models, fields, api


class CustomPurchaseOrderLine(models.Model):
    _name = "custom.purchase.order.line"
    _description = "Custom Purchase Order Line"

    name = fields.Text(string="Description", required=True)
    product_id = fields.Many2one("product.product", string="Producto")
    product_qty = fields.Float(string="Cantidad", required=True)
    ticket_id = fields.Many2one("helpdesk.ticket", string="Ticket relacionado")
    product_image = fields.Image(
        related="product_id.image_1920", string="Product Image", store=False
    )

    partner_id = fields.Many2one("res.partner", string="Proveedor")
    order_line = fields.One2many(
        "your.model.line", "order_id", string="Líneas de pedido"
    )

    
    def create_purchase_order(self):
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": self.partner_id.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": line.product_id.id,
                            "product_qty": line.quantity,
                            "price_unit": line.price_unit,
                        },
                    )
                    for line in self.order_line
                ],
            }
        )

        return {
            "type": "ir.actions.act_window",
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": purchase_order.id,
            "target": "current",
        }
