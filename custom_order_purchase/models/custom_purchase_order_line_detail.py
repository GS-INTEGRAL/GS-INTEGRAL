from odoo import models, fields


class CustomPurchaseOrderLineDetail(models.Model):
    _name = "custom.purchase.order.line.detail"
    _description = "Custom Purchase Order Line Detail"

    order_id = fields.Many2one("custom.purchase.order.line", string="Orden de compra personalizada")
    product_id = fields.Many2one("product.product", string="Producto")
    product_qty = fields.Float(string="Cantidad")
    price_unit = fields.Float(string="Precio unitario")