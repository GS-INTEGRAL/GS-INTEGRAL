# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Helpdesk_purchase_line(models.Model):
    _name = 'helpdesk_purchase_line'
    _description = 'Helpdesk_purchase_line'

    ticket_id = fields.Many2one(
        "helpdesk.ticket", string="Ticket", ondelete="cascade"
    )
    product_id = fields.Many2one("product.product", string="Producto", required=True)
    product_qty = fields.Float(string="Cantidad", default=1.0, required=True)
    