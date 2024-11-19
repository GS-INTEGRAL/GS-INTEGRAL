from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import NotFound
import logging

_logger = logging.getLogger(__name__)


class AuthSignupHomeCustom(AuthSignupHome):

    @http.route("/web/signup", type="http", auth="public", website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        _logger.info("Iniciando web_auth_signup personalizado")
        qcontext = self.get_auth_signup_qcontext()

        if "error" not in qcontext and request.httprequest.method == "POST":
            try:
                self.do_signup(qcontext)
                # Obtener el partner recién creado
                user = (
                    request.env["res.users"]
                    .sudo()
                    .search([("login", "=", qcontext.get("login"))])
                )
                partner = user.partner_id

                # Actualizar los campos personalizados
                partner.sudo().write(
                    {
                        "obra_id": qcontext.get("obra_id"),
                        "obra_secundaria": qcontext.get("obra_secundaria"),
                        "estancia_id": qcontext.get("estancia_id"),
                    }
                )

                return self.web_login(*args, **kw)
            except Exception as e:
                qcontext["error"] = str(e)

        # Proporcionar opciones para los campos de selección
        qcontext.update(
            {
                "obra_options": [
                    ("lavaqua", "Lavaqua"),
                    ("legal fincas", "Legal Fincas"),
                    ("clientes varios", "Clientes Varios"),
                    ("maristas", "Maristas"),
                ],
                "obra_secundaria_options": [
                    ("fuensanta", "Fuensanta"),
                    ("merced", "Merced"),
                ],
            }
        )

        response = request.render("auth_signup.signup", qcontext)
        response.headers["X-Frame-Options"] = "DENY"
        return response

    def get_auth_signup_qcontext(self):

        qcontext = super(AuthSignupHomeCustom, self).get_auth_signup_qcontext()

        obra_options = (
            request.env["res.partner"]
            .sudo()
            .fields_get(["obra_id"])["obra_id"]["selection"]
        )
        qcontext["obra_options"] = obra_options

        obra_id = request.params.get("obra_id")
        obra_secundaria_options = []
        if obra_id == "maristas":
            obra_secundaria_options = [
                ("fuensanta", "Fuensanta"),
                ("merced", "Merced"),
            ]
        qcontext["obra_secundaria_options"] = obra_secundaria_options

        obra_secundaria = request.params.get("obra_secundaria")
        estancia_options = self._get_estancia_options(obra_id, obra_secundaria)
        qcontext["estancia_options"] = estancia_options

        return qcontext

    def _get_estancia_options(self, obra_id, obra_secundaria=None):

        if obra_id == "maristas":
            if obra_secundaria == "fuensanta":
                return [
                    ("infantil_2_a", "Infantil 2 años - A"),
                    ("infantil_3_a", "1º Infantil 3 años - A"),
                    ("infantil_3_b", "1º Infantil 3 años - B"),
                    ("infantil_3_c", "1º Infantil 3 años - C"),
                    ("infantil_3_d", "1º Infantil 3 años - D"),
                    ("infantil_3_e", "1º Infantil 3 años - E"),
                    ("infantil_4_a", "2º Infantil 4 años - A"),
                    ("infantil_4_b", "2º Infantil 4 años - B"),
                    ("infantil_4_c", "2º Infantil 4 años - C"),
                    ("infantil_4_d", "2º Infantil 4 años - D"),
                    ("infantil_4_e", "2º Infantil 4 años - E"),
                    ("infantil_5_a", "3º Infantil 5 años - A"),
                    ("infantil_5_b", "3º Infantil 5 años - B"),
                    ("infantil_5_c", "3º Infantil 5 años - C"),
                    ("infantil_5_d", "3º Infantil 5 años - D"),
                    ("infantil_5_e", "3º Infantil 5 años - E"),
                    ("primaria_1_a", "1º Primaria - A"),
                    ("primaria_1_b", "1º Primaria - B"),
                    ("primaria_1_c", "1º Primaria - C"),
                    ("primaria_1_d", "1º Primaria - D"),
                    ("primaria_1_e", "1º Primaria - E"),
                    ("primaria_2_a", "2º Primaria - A"),
                    ("primaria_2_b", "2º Primaria - B"),
                    ("primaria_2_c", "2º Primaria - C"),
                    ("primaria_2_d", "2º Primaria - D"),
                    ("primaria_2_e", "2º Primaria - E"),
                    ("primaria_3_a", "3º Primaria - A"),
                    ("primaria_3_b", "3º Primaria - B"),
                    ("primaria_3_c", "3º Primaria - C"),
                    ("primaria_3_d", "3º Primaria - D"),
                    ("primaria_3_e", "3º Primaria - E"),
                    ("primaria_4_a", "4º Primaria - A"),
                    ("primaria_4_b", "4º Primaria - B"),
                    ("primaria_4_c", "4º Primaria - C"),
                    ("primaria_4_d", "4º Primaria - D"),
                    ("primaria_4_e", "4º Primaria - E"),
                    ("primaria_5_a", "5º Primaria - A"),
                    ("primaria_5_b", "5º Primaria - B"),
                    ("primaria_5_c", "5º Primaria - C"),
                    ("primaria_5_d", "5º Primaria - D"),
                    ("primaria_5_e", "5º Primaria - E"),
                    ("primaria_6_a", "6º Primaria - A"),
                    ("primaria_6_b", "6º Primaria - B"),
                    ("primaria_6_c", "6º Primaria - C"),
                    ("primaria_6_d", "6º Primaria - D"),
                    ("primaria_6_e", "6º Primaria - E"),
                    ("pab_aseos", "Pabellón Aseos/Vestuarios"),
                    ("pab_general", "Pabellón General"),
                    ("pab_judo", "Pabellón Judo"),
                    ("pab_terrazas", "Pabellón Terrazas y Trasteros"),
                    ("capilla", "Capilla"),
                    ("sala_medios", "Sala de Medios"),
                    ("laboratorio", "Laboratorio"),
                    ("danza", "Danza"),
                ]
            elif obra_secundaria == "merced":
                return [
                    ("eso_1_a", "1º ESO - A"),
                    ("eso_1_b", "1º ESO - B"),
                ]
        return []

    @http.route("/get_estancias", type="json", auth="public", methods=["POST"])
    def get_estancias(self):

        obra_id = request.jsonrequest.get("obra_id")
        obra_secundaria = request.jsonrequest.get("obra_secundaria")
        if not obra_id:
            return []

        estancia_options = self._get_estancia_options(obra_id, obra_secundaria)
        return estancia_options
