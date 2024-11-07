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
    attachment = fields.Image(
        string="Imagen del Producto",
        help="Adjunta una imagen del producto necesario",
    )

    # Botón para crear una orden de compra
    @api.model
    def create_purchase_order_line(self):
        # Verificar que se ha seleccionado un producto y una cantidad válida
        if not self.product_id or self.product_qty <= 0:
            raise UserError(
                _("Debe especificar un producto y una cantidad válida para la compra.")
            )

        # Crear la orden de compra o seleccionar una existente
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": self.env.user.company_id.partner_id.id,  
                "origin": self.name or _("Ticket de Helpdesk: %s") % self.id,
            }
        )

        # Crear una línea en la orden de compra
        self.env["purchase.order.line"].create(
            {
                "order_id": purchase_order.id,
                "product_id": self.product_id.id,
                "name": self.name or self.product_id.name,
                "product_qty": self.product_qty,
                "date_planned": fields.Date.today(),
            }
        )

        # Confirmar la orden de compra si es necesario
        purchase_order.button_confirm()
        return {
            "type": "ir.actions.act_window",
            "name": _("Orden de Compra"),
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": purchase_order.id,
            "target": "current",
        }
