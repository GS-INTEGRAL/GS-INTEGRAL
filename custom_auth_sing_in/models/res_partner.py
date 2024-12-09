from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    obra_id = fields.Selection(
        [
            ("lavaqua", "Lavaqua"),
            ("legal fincas", "Legal Fincas"),
            ("clientes varios", "Clientes Varios"),
            ("maristas", "Maristas"),
        ],
        string="Cliente",
    )
    obra_secundaria = fields.Char( string="Obra/sede")
    estancia_id = fields.Char( string="Estancia/Capítulo")


# class PartnerEstancia(models.Model):
#     _name = "res.partner.estancia_id"
#     _order = "name"
#     _description = "Partner Estancia"

#     name = fields.Char(string="Estancia/Capítulo", required=True, translate=True)


# class PartnerObraSecundaria(models.Model):
#     _name = "res.partner.obra_secundaria"
#     _order = "name"
#     _description = "Partner Obra Secundaria"

#     name = fields.Char(string="Obra/sede", required=True, translate=True)
    # obra_secundaria = fields.Selection(
    #     [
    #         ("fuensanta", "Fuensanta"),
    #         ("merced", "Merced"),
    #     ],
    #     string="Obra Secundaria",
    # )

    # estancia_id = fields.Selection(
    #     selection=[
    #         ("infantil_2_a", "Infantil 2 años - A"),
    #         ("infantil_3_a", "1º Infantil 3 años - A"),
    #         ("infantil_3_b", "1º Infantil 3 años - B"),
    #         ("infantil_3_c", "1º Infantil 3 años - C"),
    #         ("infantil_3_d", "1º Infantil 3 años - D"),
    #         ("infantil_3_e", "1º Infantil 3 años - E"),
    #         ("infantil_4_a", "2º Infantil 4 años - A"),
    #         ("infantil_4_b", "2º Infantil 4 años - B"),
    #         ("infantil_4_c", "2º Infantil 4 años - C"),
    #         ("infantil_4_d", "2º Infantil 4 años - D"),
    #         ("infantil_4_e", "2º Infantil 4 años - E"),
    #         ("infantil_5_a", "3º Infantil 5 años - A"),
    #         ("infantil_5_b", "3º Infantil 5 años - B"),
    #         ("infantil_5_c", "3º Infantil 5 años - C"),
    #         ("infantil_5_d", "3º Infantil 5 años - D"),
    #         ("infantil_5_e", "3º Infantil 5 años - E"),
    #         ("primaria_1_a", "1º Primaria - A"),
    #         ("primaria_1_b", "1º Primaria - B"),
    #         ("primaria_1_c", "1º Primaria - C"),
    #         ("primaria_1_d", "1º Primaria - D"),
    #         ("primaria_1_e", "1º Primaria - E"),
    #         ("primaria_2_a", "2º Primaria - A"),
    #         ("primaria_2_b", "2º Primaria - B"),
    #         ("primaria_2_c", "2º Primaria - C"),
    #         ("primaria_2_d", "2º Primaria - D"),
    #         ("primaria_2_e", "2º Primaria - E"),
    #         ("primaria_3_a", "3º Primaria - A"),
    #         ("primaria_3_b", "3º Primaria - B"),
    #         ("primaria_3_c", "3º Primaria - C"),
    #         ("primaria_3_d", "3º Primaria - D"),
    #         ("primaria_3_e", "3º Primaria - E"),
    #         ("primaria_4_a", "4º Primaria - A"),
    #         ("primaria_4_b", "4º Primaria - B"),
    #         ("primaria_4_c", "4º Primaria - C"),
    #         ("primaria_4_d", "4º Primaria - D"),
    #         ("primaria_4_e", "4º Primaria - E"),
    #         ("primaria_5_a", "5º Primaria - A"),
    #         ("primaria_5_b", "5º Primaria - B"),
    #         ("primaria_5_c", "5º Primaria - C"),
    #         ("primaria_5_d", "5º Primaria - D"),
    #         ("primaria_5_e", "5º Primaria - E"),
    #         ("primaria_6_a", "6º Primaria - A"),
    #         ("primaria_6_b", "6º Primaria - B"),
    #         ("primaria_6_c", "6º Primaria - C"),
    #         ("primaria_6_d", "6º Primaria - D"),
    #         ("primaria_6_e", "6º Primaria - E"),
    #         ("pab_aseos", "Pabellón Aseos/Vestuarios"),
    #         ("pab_general", "Pabellón General"),
    #         ("pab_judo", "Pabellón Judo"),
    #         ("pab_terrazas", "Pabellón Terrazas y Trasteros"),
    #         ("capilla", "Capilla"),
    #         ("sala_medios", "Sala de Medios"),
    #         ("laboratorio", "Laboratorio"),
    #         ("danza", "Danza"),
    #         ("eso_1_a", "1º ESO - A"),
    #         ("eso_1_b", "1º ESO - B"),
    #         ("eso_1_c", "1º ESO - C"),
    #         ("eso_1_d", "1º ESO - D"),
    #         ("eso_1_e", "1º ESO - E"),
    #         ("eso_1_f", "1º ESO - F"),
    #         ("eso_2_a", "2º ESO - A"),
    #         ("eso_2_b", "2º ESO - B"),
    #         ("eso_2_c", "2º ESO - C"),
    #         ("eso_2_d", "2º ESO - D"),
    #         ("eso_2_e", "2º ESO - E"),
    #         ("eso_2_f", "2º ESO - F"),
    #         ("eso_3_a", "3º ESO - A"),
    #         ("eso_3_b", "3º ESO - B"),
    #         ("eso_3_c", "3º ESO - C"),
    #         ("eso_3_d", "3º ESO - D"),
    #         ("eso_3_e", "3º ESO - E"),
    #         ("eso_3_f", "3º ESO - F"),
    #         ("eso_4_a", "4º ESO - A"),
    #         ("eso_4_b", "4º ESO - B"),
    #         ("eso_4_c", "4º ESO - C"),
    #         ("eso_4_d", "4º ESO - D"),
    #         ("eso_4_e", "4º ESO - E"),
    #         ("eso_4_f", "4º ESO - F"),
    #         ("bach_1_a", "1º Bachillerato - A"),
    #         ("bach_1_b", "1º Bachillerato - B"),
    #         ("bach_1_c", "1º Bachillerato - C"),
    #         ("bach_1_d", "1º Bachillerato - D"),
    #         ("bach_1_e", "1º Bachillerato - E"),
    #         ("bach_2_a", "2º Bachillerato - A"),
    #         ("bach_2_b", "2º Bachillerato - B"),
    #         ("bach_2_c", "2º Bachillerato - C"),
    #         ("bach_2_d", "2º Bachillerato - D"),
    #         ("bach_2_e", "2º Bachillerato - E"),
    #     ],
    #     string="Estancias",
    # )
