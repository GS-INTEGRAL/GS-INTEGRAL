from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    custom_purchase_order_ids = fields.One2many(
        "custom.purchase.order.line",
        "ticket_id",
        string="Líneas de compra personalizadas",
    )

    def create_purchase_order(self):
        self.ensure_one()
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": self.partner_id.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": line.product_id.id,
                            "product_qty": line.product_qty,
                            "price_unit": line.price_unit,
                        },
                    )
                    for line in self.custom_purchase_order_ids
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
