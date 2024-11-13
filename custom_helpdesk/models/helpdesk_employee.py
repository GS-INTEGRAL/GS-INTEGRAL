from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HelpdeskEmployee(models.Model):
    _inherit = "helpdesk.ticket"

    # Campos necesarios para la compra de materiales/productos
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        help="Producto que se necesita para la obra",
    )
    name = fields.Char(
        string="Descripción del Producto",
        help="Descripción detallada del producto que se necesita",
    )
    product_qty = fields.Float(
        string="Cantidad", default=1.0, help="Cantidad de producto requerida"
    )
    attachment = fields.Binary(
        string="Imagen del Producto",
        help="Adjunta una imagen del producto necesario",
    )
    attachment_filename = fields.Char("Nombre de Archivo de la Imagen")

    @api.model
    def create_purchase_order_line(self, _=None):
        """Método para crear una línea de orden de compra desde el ticket."""
        if not self.product_id or self.product_qty <= 0:
            raise UserError(
                _("Debe especificar un producto y una cantidad válida para la compra.")
            )

        # Crear la orden de compra
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": self.env.user.company_id.partner_id.id,
                "origin": self.name or _("Ticket de Helpdesk: %s") % self.id,
            }
        )

        # Crear la línea de orden de compra
        self.env["purchase.order.line"].create(
            {
                "order_id": purchase_order.id,
                "product_id": self.product_id.id,
                "name": self.name or self.product_id.name,
                "product_qty": self.product_qty,
                "price_unit": self.product_id.standard_price,
                "date_planned": fields.Date.today(),
            }
        )

        # Confirmar la orden de compra
        purchase_order.button_confirm()

        # Abrir la orden de compra generada
        return {
            "type": "ir.actions.act_window",
            "name": _("Orden de Compra"),
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": purchase_order.id,
            "target": "current",
        }

    def download_attachment(self):
        if not self.attachment:
            raise UserError(_("No hay ninguna imagen adjunta para descargar."))

        if not self.attachment_filename:
            raise UserError(_("El nombre del archivo de la imagen no está definido."))

        return {
            "type": "ir.actions.act_url",
            "url": f"/web/content/{self._name}/{self.id}/attachment/{self.attachment_filename}",
            "target": "self",
        }
