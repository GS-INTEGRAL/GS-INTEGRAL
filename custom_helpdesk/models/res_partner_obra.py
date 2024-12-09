from odoo import models, fields

class PartnerObraSecundaria(models.Model):
    _name = "res.partner.obra_secundaria"
    _order = "name"
    _description = "Partner Obra Secundaria"

    obra_secundaria = fields.Many2one(
        'res.partner.obra_secundaria', 
        string="Obra/sede"
    )
    is_obra_secundaria = fields.Boolean(default=True)
