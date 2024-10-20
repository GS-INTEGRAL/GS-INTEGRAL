from odoo import models, fields

class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    sede = fields.Char(string='Sede', help='Centro en general donde se ha producido la incidencia')
    lugar_incidencia = fields.Char(string='Lugar de Incidencia', help='Sitio exacto dentro de la sede donde se ha producido la incidencia')
    comentario_reparacion = fields.Text(string='Comentario de Reparación', help='Comentarios positivos o negativos sobre la reparación realizada por el cliente')
    observacion_mantenimiento = fields.Text(string='Observaciones de Mantenimiento', help='Observaciones del técnico sobre dudas o problemas durante la reparación')
    categoria = fields.Selection(
        [
            ('bricolage', 'Bricolaje'),
            ('fontaneria', 'Fontanería'),
            ('climatizacion', 'Climatización'),
            ('electricidad', 'Electricidad'),
        ],
        string='Categoría'
    )
    sede_imagen = fields.Binary(string='Imagen o Archivo de la Sede', attachment=True, help='Sube una imagen o archivo de la sede donde ocurrió la incidencia (PNG, JPEG, PDF)')
    lugar_incidencia_imagen = fields.Binary(string='Imagen o Archivo del Lugar de Incidencia', attachment=True, help='Sube una imagen o archivo del lugar exacto de la incidencia (PNG, JPEG, PDF)')