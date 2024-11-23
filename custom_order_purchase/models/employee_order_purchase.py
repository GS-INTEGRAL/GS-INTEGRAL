# -*- coding: utf-8 -*-
import logging

from odoo import models, fields
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class Employee_order_purchasePy(models.Model):
    _inherit = "helpdesk.ticket"

    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        required=True,
        domain=[("purchase_ok", "=", True)],  # Solo productos comprables
    )
    product_qty = fields.Float(string="Cantidad", required=True, default=1.0)
    purchase_order_id = fields.Many2one(
        "purchase.order", string="Orden de Compra Relacionada", readonly=True
    )

    def action_create_draft_purchase_order(self):
        """
        Crea una orden de compra en estado borrador con el producto y cantidad.
        """
        self.ensure_one()

        # Validar que los campos estén rellenos
        if not self.product_id or not self.product_qty:
            raise UserError(
                "Debes seleccionar un producto y una cantidad antes de enviar el pedido."
            )

        # Crear una nueva orden de compra
        purchase_order = self.env["purchase.order"].create(
            {
                "helpdesk_ticket_id": self.id,  # Enlace con el ticket
                "origin": self.name,  # Nombre del ticket como referencia
            }
        )

        # Añadir una línea de pedido con el producto y la cantidad
        self.env["purchase.order.line"].create(
            {
                "order_id": purchase_order.id,
                "product_id": self.product_id.id,
                "product_qty": self.product_qty,
                "price_unit": self.product_id.standard_price,
            }
        )

        # Enlazar el ticket con la orden creada
        self.purchase_order_id = purchase_order.id

        return {
            "type": "ir.actions.act_window",
            "name": "Orden de Compra",
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": purchase_order.id,
            "target": "new",  # Abrir en una ventana modal
        }
