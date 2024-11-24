# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class Employee_order_purchasePy(models.Model):
    _inherit = "helpdesk.ticket"

    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        # required=True,
        domain=[("id", "!=", 0)],
    )
    product_qty = fields.Float(string="Cantidad", required=True, default=1.0)
    
    # purchase_line_ids = fields.One2many(
    #     "helpdesk.purchase.line", "ticket_id", string="Líneas de Pedido"
    # )

    def action_create_draft_purchase_order(self):
        """
        Crea una orden de compra en estado borrador con el producto y cantidad.
        """
        self.ensure_one()

        if not self.purchase_line_ids:
            raise UserError(
                "Debes agregar al menos una línea de pedido antes de continuar."
            )

        partner = (
            self.purchase_line_ids[0].product_id.seller_ids
            and self.purchase_line_ids[0].product_id.seller_ids[0].partner_id
        )
        if not partner:
            raise UserError(
                "El producto seleccionado no tiene un proveedor asignado. Configura un proveedor en el producto."
            )

        # Crear una nueva orden de compra
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": partner.id,
                "helpdesk_ticket_id": self.id,
                "ticket_user_id": self.user_id.id,
                "origin": self.name,
            }
        )

        # Añadir una línea de pedido con el producto y la cantidad
        for line in self.purchase_line_ids:
            self.env["purchase.order.line"].create(
                {
                    "order_id": purchase_order.id,
                    "product_id": line.product_id.id,
                    "product_qty": line.product_qty,
                    "price_unit": line.price_unit,
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

    @api.onchange("product_id")
    def _onchange_product_id(self):
        """
        Método de depuración para verificar qué productos están disponibles.
        """
        products = self.env["product.product"].search([("purchase_ok", "=", True)])
        _logger.info(f"Productos disponibles para compra: {products}")
