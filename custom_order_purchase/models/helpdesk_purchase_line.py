from odoo import _, models, fields, api
from odoo.exceptions import UserError

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    custom_purchase_order_ids = fields.One2many(
        "custom.purchase.order.line",
        "ticket_id",
        string="Líneas de pedido",
    )

    def create_purchase_order(self):
        self.ensure_one()

        # Validar que haya líneas de compra
        if not self.custom_purchase_order_ids:
            raise UserError(_("No hay productos para crear la orden de compra."))
        
        # Buscar o crear un proveedor genérico
        Partner = self.env['res.partner']
        generic_partner = Partner.search([('name', '=', 'Proveedor Genérico')], limit=1)
        if not generic_partner:
            generic_partner = Partner.create({
                'name': 'Proveedor Genérico',
                'is_company': True,
                'supplier_rank': 1,  # Esto lo marca como proveedor
            })

        # Asignar proveedor genérico si no se ha seleccionado uno
        partner_id = generic_partner.id

        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": partner_id,
                "helpdesk_ticket_id": self.id,
                "user_id": self.user_id.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": line.product_id.id,
                            "product_qty": line.product_qty,
                            "name": line.name or line.product_id.name,
                        })for line in self.custom_purchase_order_ids
                ]
            })
        
        # self.stage_id = self.env['helpdesk.stage'].search([('name', '=', 'compra en proceso')], limit=1)

        self.clear_custom_purchase_order_lines()

        return {
            "type": "ir.actions.act_window",
            'name': 'Confirmar Orden de Compra',
            "res_model": "purchase.order.confirmation.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                'default_ticket_id': self.id,
                'default_partner_id': partner_id,
                'default_purchase_order_id': purchase_order.id 
                }   
            }


    @api.depends("custom_purchase_order_ids.product_id")
    def _compute_product_ids(self):
        for ticket in self:
            ticket.product_ids = ticket.custom_purchase_order_ids.mapped("product_id")

    product_ids = fields.Many2many(
        "product.product",
        string="Productos",
        compute="_compute_product_ids",
        store=True,
    )

    def clear_custom_purchase_order_lines(self):
    # Eliminar todas las líneas de pedido personalizadas asociadas a este ticket
        self.custom_purchase_order_ids.unlink()
