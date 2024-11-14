from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    obra_id = fields.Many2one(
        "obra", string="Sede/Obra", ondelete="set null"
    )  # Cambia 'obra' por el nombre del modelo correspondiente si existe
    estancia_id = fields.Many2one(
        "estancias.capitulo", string="Estancia/Capitulo", ondelete="set null"
    )

    @api.model
    def _add_missing_default_values(self, values):
        values = super()._add_missing_default_values(values)
        if "obra_id" not in values:
            values["obra_id"] = False
        if "estancia_id" not in values:
            values["estancia_id"] = False
        return values

    @api.model
    def create(self, vals):
        if "obra_id" in vals and not self.env["obra"].browse(vals["obra_id"]).exists():
            vals["obra_id"] = False
        if (
            "estancia_id" in vals
            and not self.env["estancias.capitulo"].browse(vals["estancia_id"]).exists()
        ):
            vals["estancia_id"] = False
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if (
            "obra_id" in vals
            and vals["obra_id"]
            and not self.env["obra"].browse(vals["obra_id"]).exists()
        ):
            vals["obra_id"] = False
        if (
            "estancia_id" in vals
            and vals["estancia_id"]
            and not self.env["estancias.capitulo"].browse(vals["estancia_id"]).exists()
        ):
            vals["estancia_id"] = False
        return super(ResPartner, self).write(vals)
