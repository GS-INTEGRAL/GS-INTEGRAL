from odoo import models, fields

class ResPartnerObraSecundaria(models.Model):
    _inherit = 'res.partner.obra_secundaria'

    # Agrega campos adicionales si necesitas
    some_new_field = fields.Char(string="Nuevo Campo Opcional")
