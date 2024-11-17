from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    obra_id = fields.Selection(
        [
            ("lavaqua", "Lavaqua"),
            ("legal fincas", "Legal Fincas"),
            ("clientes varios", "Clientes Varios"),
            ("maristas", "Maristas"),
        ],
        string="Sede-Obra",
    )
    obra_ids = fields.Many2one(
        'custom.obra',
        string="Obra Específica",
    )
    estancia_id = fields.Selection(
        selection=[],
        string="Estancias",
    )

    @api.onchange("obra_id")
    def _update_obra_ids(self):
        if self.obra_id == "maristas":
            obras = [
                ("fuensanta", "Fuensanta"),
                ("merced", "Merced"),
            ]
        else:
            obras = []
        # Guarda las opciones dinámicas para el widget Many2one
        self.env['custom.obra'].sudo().clear_obras()
        for obra in obras:
            self.env['custom.obra'].sudo().create({'name': obra[1]})

        self.obra_ids = False

    @api.onchange("obra_ids")
    def _update_estancias_id(self):
        if self.obra_ids.name == "Fuensanta":
            estancias = [
                {"name": "Infantil 2 años - A"},
                {"name": "1º Infantil 3 años - A"},
                {"name": "1º Infantil 3 años - B"},
                {"name": "1º Infantil 3 años - C"},
                {"name": "1º Infantil 3 años - D"},
                {"name": "1º Infantil 3 años - E"},
                {"name": "2º Infantil 4 años - A"},
                {"name": "2º Infantil 4 años - B"},
                {"name": "2º Infantil 4 años - C"},
                {"name": "2º Infantil 4 años - D"},
                {"name": "2º Infantil 4 años - E"},
                {"name": "3º Infantil 5 años - A"},
                {"name": "3º Infantil 5 años - B"},
                {"name": "3º Infantil 5 años - C"},
                {"name": "3º Infantil 5 años - D"},
                {"name": "3º Infantil 5 años - E"},
                {"name": "1º Primaria - A"},
                {"name": "1º Primaria - B"},
                {"name": "1º Primaria - C"},
                {"name": "1º Primaria - D"},
                {"name": "1º Primaria - E"},
                {"name": "2º Primaria - A"},
                {"name": "2º Primaria - B"},
                {"name": "2º Primaria - C"},
                {"name": "2º Primaria - D"},
                {"name": "2º Primaria - E"},
                {"name": "3º Primaria - A"},
                {"name": "3º Primaria - B"},
                {"name": "3º Primaria - C"},
                {"name": "3º Primaria - D"},
                {"name": "3º Primaria - E"},
                {"name": "4º Primaria - A"},
                {"name": "4º Primaria - B"},
                {"name": "4º Primaria - C"},
                {"name": "4º Primaria - D"},
                {"name": "4º Primaria - E"},
                {"name": "5º Primaria - A"},
                {"name": "5º Primaria - B"},
                {"name": "5º Primaria - C"},
                {"name": "5º Primaria - D"},
                {"name": "5º Primaria - E"},
                {"name": "6º Primaria - A"},
                {"name": "6º Primaria - B"},
                {"name": "6º Primaria - C"},
                {"name": "6º Primaria - D"},
                {"name": "6º Primaria - E"},
                {"name": "Pabellón Aseos/Vestuarios"},
                {"name": "Pabellón General"},
                {"name": "Pabellón Judo"},
                {"name": "Pabellón Terrazas y Trasteros"},
                {"name": "Capilla"},
                {"name": "Sala de Medios"},
                {"name": "Laboratorio"},
                {"name": "Danza"},
            ]
        elif self.obra_ids.name == "Merced":
            estancias = [
                {"name": "1º ESO - A"},
                {"name": "1º ESO - B"},
                {"name": "1º ESO - C"},
                {"name": "1º ESO - D"},
                {"name": "1º ESO - E"},
                {"name": "1º ESO - F"},
                {"name": "2º ESO - A"},
                {"name": "2º ESO - B"},
                {"name": "2º ESO - C"},
                {"name": "2º ESO - D"},
                {"name": "2º ESO - E"},
                {"name": "2º ESO - F"},
                {"name": "3º ESO - A"},
                {"name": "3º ESO - B"},
                {"name": "3º ESO - C"},
                {"name": "3º ESO - D"},
                {"name": "3º ESO - E"},
                {"name": "3º ESO - F"},
                {"name": "4º ESO - A"},
                {"name": "4º ESO - B"},
                {"name": "4º ESO - C"},
                {"name": "4º ESO - D"},
                {"name": "4º ESO - E"},
                {"name": "4º ESO - F"},
                {"name": "1º Bachillerato - A"},
                {"name": "1º Bachillerato - B"},
                {"name": "1º Bachillerato - C"},
                {"name": "1º Bachillerato - D"},
                {"name": "1º Bachillerato - E"},
                {"name": "2º Bachillerato - A"},
                {"name": "2º Bachillerato - B"},
                {"name": "2º Bachillerato - C"},
                {"name": "2º Bachillerato - D"},
                {"name": "2º Bachillerato - E"},
            ]
        else:
            estancias = []
        self.env['custom.estancia'].sudo().clear_estancias()
        for estancia in estancias:
            self.env['custom.estancia'].sudo().create(estancia)

        self.estancia_id = False
