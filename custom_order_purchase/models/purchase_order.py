from odoo import models, fields


class CustomPurchaseOrderLine(models.Model):
    _name = "custom.purchase.order.line"
    _description = "Custom Purchase Order Line"

    name = fields.Text(string="Description", required=False)
    product_id = fields.Many2one("product.product", string="Producto")
    product_qty = fields.Float(string="Cantidad", required=True)
    ticket_id = fields.Many2one("helpdesk.ticket", string="Ticket relacionado")
    product_image = fields.Image(
        related="product_id.image_1920", string="Product Image", store=False
    )

    partner_id = fields.Many2one("res.partner", string="Proveedor")
    order_line = fields.One2many(
        "custom.purchase.order.line.detail", "order_id", string="Líneas de pedido"
    )
