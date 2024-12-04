from odoo import models, fields


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    purchase_order_ids = fields.One2many("purchase.order.line", "ticket_id", string="Líneas de compra")
