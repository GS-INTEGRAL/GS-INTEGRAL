from odoo import models, fields


class Obra(models.Model):
    _name = "obra"
    _description = "Obra"

    name = fields.Char(string="Nombre de la Obra")
    estancias_ids = fields.One2many("estancias.capitulo",  string="Estancias")
    partner_ids = fields.One2many('res.partner',  string="Partners")