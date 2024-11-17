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

    estancia_id = fields.Selection(
        selection=[],
        string="Estancias",
    )

    @api.onchange("obra_id")
    def _onchange_obra(self):
        """Actualizar las opciones de estancia en función de la obra seleccionada."""
        if self.obra_id == "maristas":
            self.estancia_id = False
            return {"domain": {"estancia_id": [("id", "in", ["fuensanta", "merced"])]}}
        else:
            self.estancia_id = False
            return {"domain": {"estancia_id": []}}

    @api.onchange("estancia_id")
    def _update_estancias_id(self):

        estancias = []

        if self.obra_id and self.obra_id.name == "Maristas":

            obra_secundaria = self.obra_id.obra_secundaria

            if obra_secundaria == "Fuensanta":
                estancias = [
                    "Infantil 2 años - A",
                    "1º Infantil 3 años - A",
                    "1º Infantil 3 años - B",
                    "1º Infantil 3 años - C",
                    "1º Infantil 3 años - D",
                    "1º Infantil 3 años - E",
                    "2º Infantil 4 años - A",
                    "2º Infantil 4 años - B",
                    "2º Infantil 4 años - C",
                    "2º Infantil 4 años - D",
                    "2º Infantil 4 años - E",
                    "3º Infantil 5 años - A",
                    "3º Infantil 5 años - B",
                    "3º Infantil 5 años - C",
                    "3º Infantil 5 años - D",
                    "3º Infantil 5 años - E",
                    "1º Primaria - A",
                    "1º Primaria - B",
                    "1º Primaria - C",
                    "1º Primaria - D",
                    "1º Primaria - E",
                    "2º Primaria - A",
                    "2º Primaria - B",
                    "2º Primaria - C",
                    "2º Primaria - D",
                    "2º Primaria - E",
                    "3º Primaria - A",
                    "3º Primaria - B",
                    "3º Primaria - C",
                    "3º Primaria - D",
                    "3º Primaria - E",
                    "4º Primaria - A",
                    "4º Primaria - B",
                    "4º Primaria - C",
                    "4º Primaria - D",
                    "4º Primaria - E",
                    "5º Primaria - A",
                    "5º Primaria - B",
                    "5º Primaria - C",
                    "5º Primaria - D",
                    "5º Primaria - E",
                    "6º Primaria - A",
                    "6º Primaria - B",
                    "6º Primaria - C",
                    "6º Primaria - D",
                    "6º Primaria - E",
                    "Pabellón Aseos/Vestuarios",
                    "Pabellón General",
                    "Pabellón Judo",
                    "Pabellón Terrazas y Trasteros",
                    "Capilla",
                    "Sala de Medios",
                    "Laboratorio",
                    "Danza",
                ]
        elif obra_secundaria == "Merced":
            estancias = [
                "1º ESO - A",
                "1º ESO - B",
                "1º ESO - C",
                "1º ESO - D",
                "1º ESO - E",
                "1º ESO - F",
                "2º ESO - A",
                "2º ESO - B",
                "2º ESO - C",
                "2º ESO - D",
                "2º ESO - E",
                "2º ESO - F",
                "3º ESO - A",
                "3º ESO - B",
                "3º ESO - C",
                "3º ESO - D",
                "3º ESO - E",
                "3º ESO - F",
                "4º ESO - A",
                "4º ESO - B",
                "4º ESO - C",
                "4º ESO - D",
                "4º ESO - E",
                "4º ESO - F",
                "1º Bachillerato - A",
                "1º Bachillerato - B",
                "1º Bachillerato - C",
                "1º Bachillerato - D",
                "1º Bachillerato - E",
                "2º Bachillerato - A",
                "2º Bachillerato - B",
                "2º Bachillerato - C",
                "2º Bachillerato - D",
                "2º Bachillerato - E",
            ]

        estancia_records = self.env["custom.estancia"].search(
            [("name", "in", estancias)]
        )

        self.estancia_id = False
        return {"domain": {"estancia_id": [("id", "in", estancia_records.ids)]
                           }
                }
