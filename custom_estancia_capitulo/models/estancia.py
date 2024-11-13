from odoo import models, fields


class Estancia(models.Model):
    _name = "estancias.capitulo"
    _description = "Estancias y Planos"

    estancia = fields.Char(string="Estancia", required=True)
    plano = fields.Binary(string="Plano", attachment=True)
    plano_filename = fields.Char(string="Nombre del archivo")
