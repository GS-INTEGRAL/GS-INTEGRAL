from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound


class AuthSignupHomeCustom(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        qcontext = super().get_auth_signup_qcontext()
        for field in ["estancia_id", "obra_id"]:
            value = http.request.params.get(field)
            if value:
                try:
                    qcontext[field] = int(value)
                except ValueError:
                    qcontext[field] = value
        return qcontext

    def _prepare_signup_values(self, qcontext):
        # Llama al método original para obtener los valores básicos
        values = super()._prepare_signup_values(qcontext)

        def get_record_id(model, value):
            if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
                return int(value)
            record = request.env[model].sudo().search([("name", "=", value)], limit=1)
            return record.id if record else None

        if qcontext.get("estancia_id"):
            values["estancia_id"] = get_record_id(
                "estancias.capitulo", qcontext["estancia_id"]
            )
        if qcontext.get("obra_id"):
            values["obra_id"] = get_record_id("obra", qcontext["obra_id"])

        return values

    @http.route("/get_obra_options", type="json", auth="public")
    def get_obra_options(self, obra_id=None):
        """Devuelve opciones dinámicas para obra_ids basado en obra_id"""
        options = []
        if obra_id == "maristas":
            options = [
                {"id": "fuensanta", "name": "Fuensanta"},
                {"id": "merced", "name": "Merced"},
            ]
        return options

    @http.route("/get_estancias_options", type="json", auth="public")
    def get_estancias_options(self, obra_ids=None):
        """Devuelve opciones dinámicas para estancias_id basado en obra_ids"""
        options = []
        if obra_ids == "fuensanta":
            options = [
                {"id": "infantil_2_a", "name": "Infantil 2 años - A"},
                {"id": "infantil_2_a", "name": "Infantil 2 años - A"},
                {"id": "infantil_3_a", "name": "1º Infantil 3 años - A"},
                {"id": "infantil_3_b", "name": "1º Infantil 3 años - B"},
                {"id": "infantil_3_c", "name": "1º Infantil 3 años - C"},
                {"id": "infantil_3_d", "name": "1º Infantil 3 años - D"},
                {"id": "infantil_3_e", "name": "1º Infantil 3 años - E"},
                {"id": "infantil_4_a", "name": "2º Infantil 4 años - A"},
                {"id": "infantil_4_b", "name": "2º Infantil 4 años - B"},
                {"id": "infantil_4_c", "name": "2º Infantil 4 años - C"},
                {"id": "infantil_4_d", "name": "2º Infantil 4 años - D"},
                {"id": "infantil_4_e", "name": "2º Infantil 4 años - E"},
                {"id": "infantil_5_a", "name": "3º Infantil 5 años - A"},
                {"id": "infantil_5_b", "name": "3º Infantil 5 años - B"},
                {"id": "infantil_5_c", "name": "3º Infantil 5 años - C"},
                {"id": "infantil_5_d", "name": "3º Infantil 5 años - D"},
                {"id": "infantil_5_e", "name": "3º Infantil 5 años - E"},
                {"id": "primaria_1_a", "name": "1º Primaria - A"},
                {"id": "primaria_1_b", "name": "1º Primaria - B"},
                {"id": "primaria_1_c", "name": "1º Primaria - C"},
                {"id": "primaria_1_d", "name": "1º Primaria - D"},
                {"id": "primaria_1_e", "name": "1º Primaria - E"},
                {"id": "primaria_2_a", "name": "2º Primaria - A"},
                {"id": "primaria_2_b", "name": "2º Primaria - B"},
                {"id": "primaria_2_c", "name": "2º Primaria - C"},
                {"id": "primaria_2_d", "name": "2º Primaria - D"},
                {"id": "primaria_2_e", "name": "2º Primaria - E"},
                {"id": "primaria_3_a", "name": "3º Primaria - A"},
                {"id": "primaria_3_b", "name": "3º Primaria - B"},
                {"id": "primaria_3_c", "name": "3º Primaria - C"},
                {"id": "primaria_3_d", "name": "3º Primaria - D"},
                {"id": "primaria_3_e", "name": "3º Primaria - E"},
                {"id": "primaria_4_a", "name": "4º Primaria - A"},
                {"id": "primaria_4_b", "name": "4º Primaria - B"},
                {"id": "primaria_4_c", "name": "4º Primaria - C"},
                {"id": "primaria_4_d", "name": "4º Primaria - D"},
                {"id": "primaria_4_e", "name": "4º Primaria - E"},
                {"id": "primaria_5_a", "name": "5º Primaria - A"},
                {"id": "primaria_5_b", "name": "5º Primaria - B"},
                {"id": "primaria_5_c", "name": "5º Primaria - C"},
                {"id": "primaria_5_d", "name": "5º Primaria - D"},
                {"id": "primaria_5_e", "name": "5º Primaria - E"},
                {"id": "primaria_6_a", "name": "6º Primaria - A"},
                {"id": "primaria_6_b", "name": "6º Primaria - B"},
                {"id": "primaria_6_c", "name": "6º Primaria - C"},
                {"id": "primaria_6_d", "name": "6º Primaria - D"},
                {"id": "primaria_6_e", "name": "6º Primaria - E"},
                {"id": "pab_aseos", "name": "Pabellón Aseos/Vestuarios"},
                {"id": "pab_general", "name": "Pabellón General"},
                {"id": "pab_judo", "name": "Pabellón Judo"},
                {"id": "pab_terrazas", "name": "Pabellón Terrazas y Trasteros"},
                {"id": "capilla", "name": "Capilla"},
                {"id": "sala_medios", "name": "Sala de Medios"},
                {"id": "laboratorio", "name": "Laboratorio"},
                {"id": "danza", "name": "Danza"},
            ]
        elif obra_ids == "merced":
            options = [
                {"id": "eso_1_a", "name": "1º ESO - A"},
                {"id": "eso_1_b", "name": "1º ESO - B"},
                {"id": "eso_1_c", "name": "1º ESO - C"},
                {"id": "eso_1_d", "name": "1º ESO - D"},
                {"id": "eso_1_e", "name": "1º ESO - E"},
                {"id": "eso_1_f", "name": "1º ESO - F"},
                {"id": "eso_2_a", "name": "2º ESO - A"},
                {"id": "eso_2_b", "name": "2º ESO - B"},
                {"id": "eso_2_c", "name": "2º ESO - C"},
                {"id": "eso_2_d", "name": "2º ESO - D"},
                {"id": "eso_2_e", "name": "2º ESO - E"},
                {"id": "eso_2_f", "name": "2º ESO - F"},
                {"id": "eso_3_a", "name": "3º ESO - A"},
                {"id": "eso_3_b", "name": "3º ESO - B"},
                {"id": "eso_3_c", "name": "3º ESO - C"},
                {"id": "eso_3_d", "name": "3º ESO - D"},
                {"id": "eso_3_e", "name": "3º ESO - E"},
                {"id": "eso_3_f", "name": "3º ESO - F"},
                {"id": "eso_4_a", "name": "4º ESO - A"},
                {"id": "eso_4_b", "name": "4º ESO - B"},
                {"id": "eso_4_c", "name": "4º ESO - C"},
                {"id": "eso_4_d", "name": "4º ESO - D"},
                {"id": "eso_4_e", "name": "4º ESO - E"},
                {"id": "eso_4_f", "name": "4º ESO - F"},
                {"id": "bach_1_a", "name": "1º Bachillerato - A"},
                {"id": "bach_1_b", "name": "1º Bachillerato - B"},
                {"id": "bach_1_c", "name": "1º Bachillerato - C"},
                {"id": "bach_1_d", "name": "1º Bachillerato - D"},
                {"id": "bach_1_e", "name": "1º Bachillerato - E"},
                {"id": "bach_2_a", "name": "2º Bachillerato - A"},
                {"id": "bach_2_b", "name": "2º Bachillerato - B"},
                {"id": "bach_2_c", "name": "2º Bachillerato - C"},
                {"id": "bach_2_d", "name": "2º Bachillerato - D"},
                {"id": "bach_2_e", "name": "2º Bachillerato - E"},
            ]
        return options


class WebsiteHelpdesk(http.Controller):

    @http.route(
        ["/helpdesk/create"],
        type="http",
        auth="user",
        website=True,
    )
    def website_helpdesk(self, **kwargs):
        if request.env.user._is_public():

            return request.redirect("/web/singup?redirect=/helpdesk")

        user = request.env.user
        # Asignamos los valores de obra_id y estancia_id si están presentes en el usuario
        obra_id = user.partner_id.obra_id.id if user.partner_id.obra_id else None
        estancia_id = (
            user.partner_id.estancia_id.id if user.partner_id.estancia_id else None
        )

        # Ahora podemos pasar estos valores al formulario del ticket
        return request.render(
            "website_helpdesk.team_form_1",
            {
                "obra_id": obra_id,
                "estancia_id": estancia_id,
            },
        )


class DynamicFieldsController(http.Controller):
    @http.route("/get_obra_options", type="json", auth="public")
    def get_obra_options(self):
        """Devuelve las opciones de obra_id dinámicamente."""
        obras = request.env["custom.obra"].search([])
        return [{"id": obra.id, "name": obra.name} for obra in obras]

    @http.route("/get_obra_ids_options", type="json", auth="public")
    def get_obra_ids_options(self, obra_id):
        """Devuelve las opciones de obra_ids basado en obra_id."""
        if obra_id == "maristas":
            obras = request.env["custom.obra"].search([])
        else:
            obras = []
        return [{"id": obra.id, "name": obra.name} for obra in obras]

    @http.route("/get_estancia_options", type="json", auth="public")
    def get_estancia_options(self, obra_ids):
        """Devuelve las opciones de estancia_id basado en obra_ids."""
        estancias = request.env["custom.estancia"].search([])
        return [{"id": estancia.id, "name": estancia.name} for estancia in estancias]
