from odoo import models, fields, api
from odooError import UserError

class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    sede = fields.Char(string="Sede", related="partner_id.sede", store=True)
    lugar = fields.Char(string="Lugar", related="partner_id.lugar", store=True)
    comentario_reparacion = fields.Text(string='Comentario de Reparación', help='Comentarios positivos o negativos sobre la reparación realizada por el cliente')
    observacion_mantenimiento = fields.Text(string='Observaciones de Mantenimiento', help='Observaciones del técnico sobre dudas o problemas durante la reparación')
    categoria = fields.Selection(
        [
            ('bricolage', 'Bricolaje'),
            ('fontaneria', 'Fontanería'),
            ('climatizacion', 'Climatización'),
            ('electricidad', 'Electricidad'),
            ('albañileria', 'Albañilería'),
            ('varios', 'Varios'),
            ('tic-ordenadores', 'Tic-Ordenadores'),
            ('mantenimiento', 'Mantenimiento'),
            ('pintura', 'Pintura'),
            ('herreria', 'Herrería'),
            ('jardineria', 'Jardinería'),
            ('carpinteria', 'Carpintería'),
            ('cristaleria', 'Cristalería'),            
        ],
        string='Categoría'
    )
    
    prioridad = fields.Selection(
        [
            ('alta', 'Alta'),
            ('media', 'Media'),
            ('baja', 'Baja'),                    
        ],
        string='Prioridad'
    )
    
    estado = fields.Selection(
        [
            ('abierta', 'Abierta'),
            ('cerrado', 'Cerrado'),
            ('En proceso', 'En proceso'),
            ('baja', 'Baja'),
            ('derivada', 'Derivada'),                        
        ],
        string='Estado'
    )
    
    satisfaccion = fields.Selection(
        [
            ('positiva', 'Positiva'),
            ('negativa', 'Negativa'),
        ],
        string='Satisfacción'
    )
    
    sede_imagen = fields.Binary(string='Imagen o Archivo de la Sede', attachment=True, help='Sube una imagen o archivo de la sede donde ocurrió la incidencia (PNG, JPEG, PDF)')
    lugar_incidencia_imagen = fields.Binary(string='Imagen o Archivo del Lugar de Incidencia', attachment=True, help='Sube una imagen o archivo del lugar exacto de la incidencia (PNG, JPEG, PDF)')
    fecha_fin = fields.Date(string="Fecha Finalización")

    @api.onchange('estado')
    def _onchange_estado(self):
        print("Estado cambiado:", self.estado)
        if self.estado in ['cerrado', 'baja', 'derivada']:
            self.fecha_fin = fields.Date.today()
        else:
            self.fecha_fin = False
            
    @api.onchange('prioridad')
    def _onchange_prioridad(self):
        if self.prioridad == 'Alta':
            self._enviar_email_prioridad_alta()
    
    def _enviar_email_prioridad_alta(self):
        """Envía un correo electrónico al administrador cuando la prioridad es alta."""
        admin = self.env.ref('base.user_admin')
        if not admin.email:
            raise UserError("El usuario administrador no tiene un correo electrónico configurado.")
    
        ticket_num = self.id
        ticket_description = self.name or 'Sin descripción'
        opened_by = self.partner_id.name or 'Desconocido'
        opened_email = self.partner_id.email or 'Sin correo'

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
            'subject': subject,
            'body_html': body_html,
            'email_to': admin.email,
            'email_from': self.env.user.email,  
        }
        mail = self.env['mail.mail'].create(mail_values)
        mail.send()