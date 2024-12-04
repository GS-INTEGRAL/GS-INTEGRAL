from odoo import models, fields


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    custom_purchase_order_ids = fields.One2many(
        "custom.purchase.order.line",
        "ticket_id",
        string="Líneas de compra personalizadas",
    )
