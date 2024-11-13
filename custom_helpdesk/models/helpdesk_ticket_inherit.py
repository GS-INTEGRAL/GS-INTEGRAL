import string
from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicketInherit(models.Model):
    _inherit = "helpdesk.ticket"

    estancia_id = fields.Many2one("estancias.capitulo", string="Estancia")
    obra_id = fields.Many2one("obra", string="Obra")
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
    )
    lugar_incidencia_imagen = fields.Binary(
        string="Imagen o Archivo del Lugar de Incidencia",
        attachment=True,
    )
    fecha_fin = fields.Date(string="Fecha Finalización")
    email = fields.Char(
        string="Correo Electrónico",
        help="Correo electrónico ingresado en el formulario web",
    )

    @api.model
    def create(self, vals):
        # Si el usuario tiene valores para obra_id y estancia_id, los asignamos al ticket
        if self.env.user.partner_id.obra_id:
            vals["obra_id"] = self.env.user.partner_id.obra_id.id
        if self.env.user.partner_id.estancia_id:
            vals["estancia_id"] = self.env.user.partner_id.estancia_id.id

        return super(HelpdeskTicket, self).create(vals)

    @api.onchange("stage_id")
    def _onchange_stage_id(self):
        resolved_stage_id = self.env.ref("helpdesk.stage_solved").id
        canceled_stage_id = 5

        if self.stage_id.id in [resolved_stage_id, canceled_stage_id]:
            if not self.fecha_fin:
                self.fecha_fin = fields.Date.today()
        else:
            self.fecha_fin = False

    @api.onchange("obra_id")
    def _onchange_obra_id(self):
        if self.obra_id:
            return {"domain": {"estancia_id": [("obra_id", "=", self.obra_id.id)]}}
        else:
            return {"domain": {"estancia_id": []}}

    # def create(self, vals_list):
    #     # Asegúrate de que `vals_list` sea una lista
    #     if not isinstance(vals_list, list):
    #         vals_list = [vals_list]

    #     # Iterar sobre cada conjunto de valores en `vals_list`
    #     for vals in vals_list:
    #         # Si hay un `partner_id`, asigna su email a `email_cc`
    #         if vals.get("partner_id"):
    #             partner = self.env["res.partner"].browse(vals["partner_id"])
    #             vals["email_cc"] = partner.email

    #     # Crear el ticket llamando a `super`
    #     tickets = super().create(vals_list)

    #     # Enviar correo electrónico a cada ticket creado con `email_cc`
    #     for ticket in tickets:
    #         if ticket.email_cc:
    #             # Publicar mensaje y enviar notificación por correo electrónico
    #             ticket.message_post(
    #                 subject="Nuevo ticket creado",
    #                 body="Se ha creado un nuevo ticket en el sistema de soporte.",
    #                 partner_ids=[ticket.partner_id.id] if ticket.partner_id else [],
    #                 email_layout_xmlid="mail.mail_notification_light",
    #                 subtype_id=self.env.ref("mail.mt_comment").id,
    #             )

    #     return tickets

    # def write(self, vals):
    #     # Si se está actualizando el partner_id, actualizamos el email_cc
    #     if "partner_id" in vals:
    #         partner = self.env["res.partner"].browse(vals["partner_id"])
    #         vals["email_cc"] = partner.email
    #     return super().write(vals)

    # @api.onchange("prioridad")
    # def _onchange_prioridad(self):
    #     if self.prioridad == "alta" and not self._context.get('from_email_trigger', False):
    #         self._enviar_email_prioridad_alta()

    # def _enviar_email_prioridad_alta(self):
    #     admin = self.env.ref("base.user_admin", raise_if_not_found=False)
    #     if not admin.email or not admin.email:
    #         raise UserError(
    #             "El usuario administrador no tiene un correo electrónico configurado."
    #         )

    #     ticket_num = self.id
    #     ticket_description = self.name or "Sin descripción"
    #     opened_by = self.partner_id.name or "Desconocido"
    #     opened_email = self.partner_id.email or "Sin correo"

    #     subject = f"Alerta: Ticket {ticket_num} con Prioridad Alta"
    #     body_html = f"""
    #         <p>¡Alerta! Se ha creado o actualizado un ticket con prioridad <strong>Alta</strong>.</p>
    #         <ul>
    #             <li><strong>Número de Ticket:</strong> {ticket_num}</li>
    #             <li><strong>Descripción:</strong> {ticket_description}</li>
    #             <li><strong>Creado por:</strong> {opened_by}</li>
    #             <li><strong>Email del Creador:</strong> {opened_email}</li>
    #         </ul>
    #         <p>Por favor, revisa el ticket con urgencia.</p>
    #     """

    #     mail_values = {
    #         "subject": subject,
    #         "body_html": body_html,
    #         "email_to": admin.email,
    #         "email_from": self.env.user.email,
    #     }
    #     mail = self.env["mail.mail"].create(mail_values)
    #     mail.send()
