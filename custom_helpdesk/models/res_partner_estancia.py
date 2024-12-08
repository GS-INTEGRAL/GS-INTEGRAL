from odoo import models, fields

class ResPartnerEstancia(models.Model):
    _inherit = 'res.partner.estancia_id'

    # Agrega campos adicionales si necesitas
    another_field = fields.Boolean(string="Otro Campo Adicional")
