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
    obra_id = fields.Selection(related="partner_id.obra_id", string="Cliente")
    obra_secundaria = fields.Char(string="Sedes")
    obras = fields.Selection(
        [
            ("fuensanta", "Fuensanta"),
            ("merced", "Merced"),
        ],
        string="Obra/Sede",
    )

    estanciasid = fields.Selection(
        selection=[
            ("infantil_2_a", "Infantil 2 años - A"),
            ("infantil_3_a", "1º Infantil 3 años - A"),
            ("infantil_3_b", "1º Infantil 3 años - B"),
            ("infantil_3_c", "1º Infantil 3 años - C"),
            ("infantil_3_d", "1º Infantil 3 años - D"),
            ("infantil_3_e", "1º Infantil 3 años - E"),
            ("infantil_4_a", "2º Infantil 4 años - A"),
            ("infantil_4_b", "2º Infantil 4 años - B"),
            ("infantil_4_c", "2º Infantil 4 años - C"),
            ("infantil_4_d", "2º Infantil 4 años - D"),
            ("infantil_4_e", "2º Infantil 4 años - E"),
            ("infantil_5_a", "3º Infantil 5 años - A"),
            ("infantil_5_b", "3º Infantil 5 años - B"),
            ("infantil_5_c", "3º Infantil 5 años - C"),
            ("infantil_5_d", "3º Infantil 5 años - D"),
            ("infantil_5_e", "3º Infantil 5 años - E"),
            ("primaria_1_a", "1º Primaria - A"),
            ("primaria_1_b", "1º Primaria - B"),
            ("primaria_1_c", "1º Primaria - C"),
            ("primaria_1_d", "1º Primaria - D"),
            ("primaria_1_e", "1º Primaria - E"),
            ("primaria_2_a", "2º Primaria - A"),
            ("primaria_2_b", "2º Primaria - B"),
            ("primaria_2_c", "2º Primaria - C"),
            ("primaria_2_d", "2º Primaria - D"),
            ("primaria_2_e", "2º Primaria - E"),
            ("primaria_3_a", "3º Primaria - A"),
            ("primaria_3_b", "3º Primaria - B"),
            ("primaria_3_c", "3º Primaria - C"),
            ("primaria_3_d", "3º Primaria - D"),
            ("primaria_3_e", "3º Primaria - E"),
            ("primaria_4_a", "4º Primaria - A"),
            ("primaria_4_b", "4º Primaria - B"),
            ("primaria_4_c", "4º Primaria - C"),
            ("primaria_4_d", "4º Primaria - D"),
            ("primaria_4_e", "4º Primaria - E"),
            ("primaria_5_a", "5º Primaria - A"),
            ("primaria_5_b", "5º Primaria - B"),
            ("primaria_5_c", "5º Primaria - C"),
            ("primaria_5_d", "5º Primaria - D"),
            ("primaria_5_e", "5º Primaria - E"),
            ("primaria_6_a", "6º Primaria - A"),
            ("primaria_6_b", "6º Primaria - B"),
            ("primaria_6_c", "6º Primaria - C"),
            ("primaria_6_d", "6º Primaria - D"),
            ("primaria_6_e", "6º Primaria - E"),
            ("pab_aseos", "Pabellón Aseos/Vestuarios"),
            ("pab_general", "Pabellón General"),
            ("pab_judo", "Pabellón Judo"),
            ("pab_terrazas", "Pabellón Terrazas y Trasteros"),
            ("capilla", "Capilla"),
            ("sala_medios", "Sala de Medios"),
            ("laboratorio", "Laboratorio"),
            ("danza", "Danza"),
            ("eso_1_a", "1º ESO - A"),
            ("eso_1_b", "1º ESO - B"),
            ("eso_1_c", "1º ESO - C"),
            ("eso_1_d", "1º ESO - D"),
            ("eso_1_e", "1º ESO - E"),
            ("eso_1_f", "1º ESO - F"),
            ("eso_2_a", "2º ESO - A"),
            ("eso_2_b", "2º ESO - B"),
            ("eso_2_c", "2º ESO - C"),
            ("eso_2_d", "2º ESO - D"),
            ("eso_2_e", "2º ESO - E"),
            ("eso_2_f", "2º ESO - F"),
            ("eso_3_a", "3º ESO - A"),
            ("eso_3_b", "3º ESO - B"),
            ("eso_3_c", "3º ESO - C"),
            ("eso_3_d", "3º ESO - D"),
            ("eso_3_e", "3º ESO - E"),
            ("eso_3_f", "3º ESO - F"),
            ("eso_4_a", "4º ESO - A"),
            ("eso_4_b", "4º ESO - B"),
            ("eso_4_c", "4º ESO - C"),
            ("eso_4_d", "4º ESO - D"),
            ("eso_4_e", "4º ESO - E"),
            ("eso_4_f", "4º ESO - F"),
            ("bach_1_a", "1º Bachillerato - A"),
            ("bach_1_b", "1º Bachillerato - B"),
            ("bach_1_c", "1º Bachillerato - C"),
            ("bach_1_d", "1º Bachillerato - D"),
            ("bach_1_e", "1º Bachillerato - E"),
            ("bach_2_a", "2º Bachillerato - A"),
            ("bach_2_b", "2º Bachillerato - B"),
            ("bach_2_c", "2º Bachillerato - C"),
            ("bach_2_d", "2º Bachillerato - D"),
            ("bach_2_e", "2º Bachillerato - E"),
        ],
        string="Estancias",
    )

    estancia_id = fields.Char(string="Estancias/Capítulo")
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
        store=True,
    )

    fecha_fin = fields.Date(string="Fecha Finalización")

    is_maristas = fields.Boolean(
        string="Es Maristas",
        compute="_compute_is_maristas",
        store=True,
        help="Determina si la compañía asociada es Maristas.",
    )

    @api.depends("company_id")
    def _compute_is_maristas(self):
        for record in self:
            record.is_maristas = (
                record.company_id and record.company_id.name == "Maristas"
            )

    def write(self, vals):
        res = super().write(vals)

        # Verificamos si el estado cambió a "Resuelto"
        resolved_stage_id = self.env.ref("helpdesk.stage_solved").id
        if vals.get("stage_id") == resolved_stage_id:
            for ticket in self:
                if ticket.partner_id:
                    # Obtener la plantilla de correo
                    template = self.env["mail.template"].search(
                        [
                            (
                                "name",
                                "=",
                                "Servicio de asistencia: ticket cerrado (copia)",
                            )
                        ],
                        limit=1,
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

    @api.model
    def create(self, vals):
        if not self.env.user.company_id:
            raise UserError(
                "No tiene asignada una compañía. Por favor, contacte con el administrador al correo fran@gs-integral.com."
            )
        
        if isinstance(vals_list, dict):  
            vals_list = [vals_list]

        records = super().create(vals_list)
        return records
