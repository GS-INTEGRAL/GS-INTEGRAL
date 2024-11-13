from odoo import models, fields


class Estancia(models.Model):
    _name = "estancias.capitulo"
    _description = "Estancias y Planos"

    estancia = fields.Char(string="Estancia", required=True)
    plano = fields.Binary(string="Plano", attachment=True)
    bra_id = fields.Many2one('obra', string="Obra")  
    partner_id = fields.Many2one('res.partner', string="Asignado a")