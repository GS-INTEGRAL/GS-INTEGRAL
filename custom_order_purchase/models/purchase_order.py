# -*- coding: utf-8 -*-
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Purchase_order(models.Model):
    _inherit = "purchase.order"

    helpdesk_ticket_id = fields.Many2one(
        "helpdesk.ticket", string="Ticket de Helpdesk"
        )
