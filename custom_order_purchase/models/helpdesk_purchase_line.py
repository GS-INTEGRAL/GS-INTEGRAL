from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    custom_purchase_order_ids = fields.One2many(
        "custom.purchase.order.line",
        "ticket_id",
        string="Líneas de compra personalizadas",
    )

    @api.depends("custom_purchase_order_ids.product_id")
    def _compute_product_ids(self):
        for ticket in self:
            ticket.product_ids = ticket.custom_purchase_order_ids.mapped("product_id")

    product_ids = fields.Many2many(
        "product.product",
        string="Productos",
        compute="_compute_product_ids",
        store=True,
    )
