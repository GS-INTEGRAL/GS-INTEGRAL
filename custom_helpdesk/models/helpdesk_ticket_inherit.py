import string
from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicketInherit(models.Model):
    _inherit = "helpdesk.ticket"

    sede = fields.Char(string="Sede", related="partner_id.sede", store=True)
    lugar = fields.Char(string="Lugar", related="partner_id.lugar", store=True)
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

    prioridad = fields.Selection(
        [
            ("alta", "Alta"),
            ("media", "Media"),
            ("baja", "Baja"),
        ],
        string="Prioridad",
    )

    satisfaccion = fields.Selection(
        [
            ("positiva", "Positiva"),
            ("negativa", "Negativa"),
        ],
        string="Satisfacción",
    )

    sede_imagen = fields.Binary(
        string="Imagen o Archivo de la Sede",
        attachment=True,
        help="Sube una imagen o archivo de la sede donde ocurrió la incidencia (PNG, JPEG, PDF)",
    )
    lugar_incidencia_imagen = fields.Binary(
        string="Imagen o Archivo del Lugar de Incidencia",
        attachment=True,
        help="Sube una imagen o archivo del lugar exacto de la incidencia (PNG, JPEG, PDF)",
    )
    fecha_fin = fields.Date(string="Fecha Finalización")
    email = fields.Char(
        string="Correo Electrónico",
        help="Correo electrónico ingresado en el formulario web",
    )

    @api.onchange("stage_id")
    def _onchange_stage_id(self):
        resolved_stage_id = self.env.ref("helpdesk.stage_solved").id
        canceled_stage_id = 5

        if self.stage_id.id in [resolved_stage_id, canceled_stage_id]:
            if not self.fecha_fin:
                self.fecha_fin = fields.Date.today()
        else:
            self.fecha_fin = False

    def create(self, vals):
        # Si partner_id está presente, copiamos su email a email_cc
        if vals.get("partner_id"):
            partner = self.env["res.partner"].browse(vals["partner_id"])
            vals["email_cc"] = partner.email
        return super().create(vals)

    def write(self, vals):
        # Si se está actualizando el partner_id, actualizamos el email_cc
        if "partner_id" in vals:
            partner = self.env["res.partner"].browse(vals["partner_id"])
            vals["email_cc"] = partner.email
        return super().write(vals)

    @api.onchange("prioridad")
    def _onchange_prioridad(self):
        if self.prioridad == "alta":
            self._enviar_email_prioridad_alta()

    def _enviar_email_prioridad_alta(self):
        admin = self.env.ref("base.user_admin")
        if not admin.email:
            raise UserError(
                "El usuario administrador no tiene un correo electrónico configurado."
            )

        ticket_num = self.id
        ticket_description = self.name or "Sin descripción"
        opened_by = self.partner_id.name or "Desconocido"
        opened_email = self.partner_id.email or "Sin correo"

        subject = f"Alerta: Ticket {ticket_num} con Prioridad Alta"
        body_html = f"""
            <p>¡Alerta! Se ha creado o actualizado un ticket con prioridad <strong>Alta</strong>.</p>
            <ul>
                <li><strong>Número de Ticket:</strong> {ticket_num}</li>
                <li><strong>Descripción:</strong> {ticket_description}</li>
                <li><strong>Creado por:</strong> {opened_by}</li>
                <li><strong>Email del Creador:</strong> {opened_email}</li>
            </ul>
            <p>Por favor, revisa el ticket con urgencia.</p>
        """

        mail_values = {
            "subject": subject,
            "body_html": body_html,
            "email_to": admin.email,
            "email_from": self.env.user.email,
        }
        mail = self.env["mail.mail"].create(mail_values)
        mail.send()


class HelpdeskEmployee(models.Model):
    _inherit = "helpdesk.ticket"

    material_name = fields.Char(
        string="Material", help="Materiales necesarios para la obra", required=True
    )
    quantity = fields.Float(
        string="Cantidad", default=1.0, help="Cantidad del material requerido"
    )
    model = fields.Char(string="Modelo", help="Modelo del material")
    attachment = fields.Image(
        string="Imagen del Material",
        help="Adjunta una imagen del material si es necesario",
    )
