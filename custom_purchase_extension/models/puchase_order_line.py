from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

_logger.info("Cargando modelo PurchaseOrderLine")


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_image = fields.Image(
        related="product_id.image_1920", string="Product Image", store=False
    )
