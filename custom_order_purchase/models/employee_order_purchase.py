# -*- coding: utf-8 -*-
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Employee_order_purchasePy(models.Model):
    _inherit = "helpdesk.ticket"
    _name = "employee_order_purchase.py"
    _description = "Employee_order_purchasePy"

    purchase_order_ids = fields.One2many(
        "purchase.order", "helpdesk_ticket_id", string="Órdenes de Compra"
    )

    def action_create_purchase_order(self):
        """
        Crea una orden de compra desde el ticket de Helpdesk y la asocia.
        """
        self.ensure_one()  # Asegurarse de que solo afecta a un registro
        purchase_order = self.env["purchase.order"].create(
            {
                "helpdesk_ticket_id": self.id,  # Asociar con el ticket
                "origin": self.name,  # Usar el nombre del ticket como origen
                "partner_id": False,  # Cliente vacío al inicio
            }
        )
        return {
            "type": "ir.actions.act_window",
            "name": "Orden de Compra",
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": purchase_order.id,
            "target": "new",  # Para abrir en un modal
        }
