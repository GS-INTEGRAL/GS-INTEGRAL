import string
from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicketInherit(models.Model):
    _inherit = "helpdesk.ticket"

    partner_id = fields.Many2one("res.partner", string="Partner")
    obra_id = fields.Selection(related="partner_id.obra_id", string="Sede-Obra")
    estancia_id = fields.Selection(related="partner_id.estancia_id", string="Estancia")
    comentario_reparacion = fields.Text(
        string="Comentario de Reparación",
        help="Comentarios positivos o negativos sobre la reparación realizada por el cliente",
    )
    observacion_mantenimiento = fields.Text(
        string="Observaciones de Mantenimiento",
        help="Observaciones del técnico sobre dudas o problemas durante la reparación",
    )
    categoria = fields.Selection(
        [
            ("bricolage", "Bricolaje"),
            ("fontaneria", "Fontanería"),
            ("climatizacion", "Climatización"),
            ("electricidad", "Electricidad"),
            ("albañileria", "Albañilería"),
            ("varios", "Varios"),
            ("tic-ordenadores", "Tic-Ordenadores"),
            ("mantenimiento", "Mantenimiento"),
            ("pintura", "Pintura"),
            ("herreria", "Herrería"),
            ("jardineria", "Jardinería"),
            ("carpinteria", "Carpintería"),
            ("cristaleria", "Cristalería"),
        ],
        string="Categoría",
    )

    fecha_fin = fields.Date(string="Fecha Finalización")

    # @api.model
    # def create(self, vals):
    #     if self.env.user.partner_id.obra_id:
    #         vals["obra_id"] = self.env.user.partner_id.obra_id.id
    #     if self.env.user.partner_id.estancia_id:
    #         vals["estancia_id"] = self.env.user.partner_id.estancia_id.id

    #     return super(HelpdeskTicketInherit, self).create(vals)

    @api.onchange("stage_id")
    def _onchange_stage_id(self):
        resolved_stage_id = self.env.ref("helpdesk.stage_solved").id
        canceled_stage_id = 5

        if self.stage_id.id in [resolved_stage_id, canceled_stage_id]:
            if not self.fecha_fin:
                self.fecha_fin = fields.Date.today()
        else:
            self.fecha_fin = False

    # @api.onchange("obra_id")
    # def _onchange_obra_id(self):
    #     if self.obra_id:
    #         return {"domain": {"estancia_id": [("obra_id", "=", self.obra_id.id)]}}
    #     else:
    #         return {"domain": {"estancia_id": []}}
