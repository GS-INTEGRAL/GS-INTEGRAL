from odoo import fields, models, api


class CustomObra(models.Model):
    _name = "custom.obra"
    _description = "Opciones de Obras Dinámicas"

    name = fields.Char("Nombre")

    @api.model
    def clear_obras(self):
        """Limpia las obras existentes."""
        self.search([]).unlink()