from odoo import fields, models, api


class CustomEstancia(models.Model):
    _name = "custom.estancia"
    _description = "Opciones de Estancias Dinámicas"

    name = fields.Char("Nombre")

    @api.model
    def clear_estancias(self):
        """Limpia las estancias existentes."""
        self.search([]).unlink()
