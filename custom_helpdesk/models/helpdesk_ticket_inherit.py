import string
from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicketInherit(models.Model):
    _inherit = "helpdesk.ticket"

    images = fields.Many2many(
        "ir.attachment",
        string="Imágenes de reparaciones :",
        help="Imágenes relacionadas con el ticket.",
        domain=[("mimetype", "like", "image/")],
    )
    partner_id = fields.Many2one("res.partner", string="Partner")
<<<<<<< HEAD
    obra_id = fields.Selection(related="partner_id.obra_id", string="Sede-Obra")
    obra_secundaria = fields.Many2one(
        "sedes", string="Sede/Obra"
=======
    obra_id = fields.Selection(related="partner_id.obra_id", string="Cliente")
    obra_secundaria = fields.Selection(
        related="partner_id.obra_secundaria", string="Sede/Obra"
>>>>>>> a90576f6008a7fb81358bc58923132ce427e0878
    )
    estancia_id = fields.Many2one(
        "estancias", string="Estancia/Capítulo"
    )
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

    def write(self, vals):
        res = super().write(vals)

        # Verificamos si el estado cambió a "Resuelto"
        resolved_stage_id = self.env.ref("helpdesk.stage_solved").id
        if vals.get("stage_id") == resolved_stage_id:
            for ticket in self:
                if ticket.partner_id:
                    # Obtener la plantilla de correo
                    template = self.env['mail.template'].search(
                        [('name', '=', 'Servicio de asistencia: ticket cerrado (copia)')], 
                        limit=1
                    )
                    if not template:
                        raise UserError(
                            "No se encontró la plantilla 'Helpdesk: Ticket Closed'."
                        )

                    # Crear una copia dinámica de la plantilla y enviar el correo
                    email_values = {
                        "attachment_ids": [(6, 0, ticket.images.ids)],
                    }
                    template.send_mail(
                        ticket.id, email_values=email_values, force_send=True
                    )

        return res

    @api.onchange("stage_id")
    def _onchange_stage_id(self):
        resolved_stage_id = self.env.ref("helpdesk.stage_solved").id
        canceled_stage_id = 5

        if self.stage_id.id in [resolved_stage_id, canceled_stage_id]:
            if not self.fecha_fin:
                self.fecha_fin = fields.Date.today()
        else:
            self.fecha_fin = False
