from odoo import models, fields

class PartnerEstancia(models.Model):
    _name = "res.partner.estancia_id"
    _order = "name"
    _description = "Partner Estancia"

    estancia_id = fields.Many2one(
        'res.partner.estancia_id', 
        string="Estancia/Capítulo"
    )
    is_estancia = fields.Boolean(default=True)