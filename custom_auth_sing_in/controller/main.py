from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound
import logging

_logger = logging.getLogger(__name__)


class AuthSignupHomeCustom(AuthSignupHome):

    @http.route("/web/signup", type="http", auth="public", website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        _logger.info("Iniciando web_auth_signup personalizado")
        qcontext = self.get_auth_signup_qcontext()

        if not qcontext.get("token") and not qcontext.get("signup_enabled"):
            raise werkzeug.exceptions.NotFound()

        if "error" not in qcontext and request.httprequest.method == "POST":
            try:
                self.do_signup(qcontext)
                # Send an account creation confirmation email
                if qcontext.get("token"):
                    User = request.env["res.users"]
                    user_sudo = User.sudo().search(
                        User._get_login_domain(qcontext.get("login")),
                        order=User._get_login_order(),
                        limit=1,
                    )
                    template = request.env.ref(
                        "auth_signup.mail_template_user_signup_account_created",
                        raise_if_not_found=False,
                    )
                    if user_sudo and template:
                        template.sudo().send_mail(user_sudo.id, force_send=True)
                return self.web_login(*args, **kw)
            except UserError as e:
                qcontext["error"] = e.args[0]
            except (SignupError, AssertionError) as e:
                if (
                    request.env["res.users"]
                    .sudo()
                    .search([("login", "=", qcontext.get("login"))])
                ):
                    qcontext["error"] = _(
                        "Another user is already registered using this email address."
                    )
                else:
                    _logger.error("%s", e)
                    qcontext["error"] = _("Could not create a new account.")

        response = request.render("auth_signup.signup", qcontext)
        response.headers["X-Frame-Options"] = "DENY"
        return response

    def get_auth_signup_qcontext(self):
        _logger.info("Iniciando get_auth_signup_qcontext")
        qcontext = super(AuthSignupHomeCustom, self).get_auth_signup_qcontext()
        if qcontext is None:
            qcontext = {}

        # Obtener las opciones de obra
        obra_options = (
            request.env["res.partner"]
            .sudo()
            .fields_get(["obra_id"])["obra_id"]["selection"]
        )
        qcontext["obra_options"] = obra_options

        # Obtener las opciones de estancia basadas en la obra seleccionada
        obra_id = request.params.get("obra_id")
        if obra_id:
            estancia_options = self._get_estancia_options(obra_id)
            qcontext["estancia_options"] = estancia_options

        return qcontext

    def _get_estancia_options(self, obra_id):
        if obra_id == "maristas":
            obra_secundaria = request.params.get("obra_secundaria")
            if obra_secundaria == "fuensanta":
                return [
                    ("infantil_2_a", "Infantil 2 años - A"),
                    ("infantil_3_a", "1º Infantil 3 años - A"),
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
                    # ... (resto de las opciones para Merced)
                ]
        return []

    def _prepare_signup_values(self, qcontext):
        values = super(AuthSignupHomeCustom, self)._prepare_signup_values(qcontext)

        for field in ["obra_id", "estancia_id"]:
            if qcontext.get(field):
                values[field] = qcontext[field]

        return values

    # def get_auth_signup_qcontext(self):
    #     try:
    #         _logger.info("Iniciando get_auth_signup_qcontext")
    #         # Llama al método original para obtener el contexto de la autenticación
    #         qcontext = super().get_auth_signup_qcontext()
    #         if qcontext is None:
    #             qcontext = {}

    #         for field in ["estancia_id", "obra_id"]:
    #             value = http.request.params.get(field)
    #             if value:
    #                 try:
    #                     qcontext[field] = int(value)
    #                 except ValueError:
    #                     qcontext[field] = value

    #         # Configuración específica para 'obra_id' igual a "maristas"
    #         if qcontext.get("obra_id") == "maristas":
    #             obra_id = (
    #                 request.env["res.partner"]
    #                 .sudo()
    #                 .search([("id", "=", qcontext["obra_id"])])
    #             )
    #             if obra_id and obra_id.name == "Maristas":
    #                 obra_secundaria = http.request.params.get("obra_secundaria")
    #                 if obra_secundaria == "fuensanta":
    #                     qcontext["estancia_options"] = [
    #                         ("infantil_2_a", "Infantil 2 años - A"),
    #                         ("infantil_2_a", "Infantil 2 años - A"),
    #                         ("infantil_3_a", "1º Infantil 3 años - A"),
    #                         ("infantil_3_b", "1º Infantil 3 años - B"),
    #                         ("infantil_3_c", "1º Infantil 3 años - C"),
    #                         ("infantil_3_d", "1º Infantil 3 años - D"),
    #                         ("infantil_3_e", "1º Infantil 3 años - E"),
    #                         ("infantil_4_a", "2º Infantil 4 años - A"),
    #                         ("infantil_4_b", "2º Infantil 4 años - B"),
    #                         ("infantil_4_c", "2º Infantil 4 años - C"),
    #                         ("infantil_4_d", "2º Infantil 4 años - D"),
    #                         ("infantil_4_e", "2º Infantil 4 años - E"),
    #                         ("infantil_5_a", "3º Infantil 5 años - A"),
    #                         ("infantil_5_b", "3º Infantil 5 años - B"),
    #                         ("infantil_5_c", "3º Infantil 5 años - C"),
    #                         ("infantil_5_d", "3º Infantil 5 años - D"),
    #                         ("infantil_5_e", "3º Infantil 5 años - E"),
    #                         ("primaria_1_a", "1º Primaria - A"),
    #                         ("primaria_1_b", "1º Primaria - B"),
    #                         ("primaria_1_c", "1º Primaria - C"),
    #                         ("primaria_1_d", "1º Primaria - D"),
    #                         ("primaria_1_e", "1º Primaria - E"),
    #                         ("primaria_2_a", "2º Primaria - A"),
    #                         ("primaria_2_b", "2º Primaria - B"),
    #                         ("primaria_2_c", "2º Primaria - C"),
    #                         ("primaria_2_d", "2º Primaria - D"),
    #                         ("primaria_2_e", "2º Primaria - E"),
    #                         ("primaria_3_a", "3º Primaria - A"),
    #                         ("primaria_3_b", "3º Primaria - B"),
    #                         ("primaria_3_c", "3º Primaria - C"),
    #                         ("primaria_3_d", "3º Primaria - D"),
    #                         ("primaria_3_e", "3º Primaria - E"),
    #                         ("primaria_4_a", "4º Primaria - A"),
    #                         ("primaria_4_b", "4º Primaria - B"),
    #                         ("primaria_4_c", "4º Primaria - C"),
    #                         ("primaria_4_d", "4º Primaria - D"),
    #                         ("primaria_4_e", "4º Primaria - E"),
    #                         ("primaria_5_a", "5º Primaria - A"),
    #                         ("primaria_5_b", "5º Primaria - B"),
    #                         ("primaria_5_c", "5º Primaria - C"),
    #                         ("primaria_5_d", "5º Primaria - D"),
    #                         ("primaria_5_e", "5º Primaria - E"),
    #                         ("primaria_6_a", "6º Primaria - A"),
    #                         ("primaria_6_b", "6º Primaria - B"),
    #                         ("primaria_6_c", "6º Primaria - C"),
    #                         ("primaria_6_d", "6º Primaria - D"),
    #                         ("primaria_6_e", "6º Primaria - E"),
    #                         ("pab_aseos", "Pabellón Aseos/Vestuarios"),
    #                         ("pab_general", "Pabellón General"),
    #                         ("pab_judo", "Pabellón Judo"),
    #                         ("pab_terrazas", "Pabellón Terrazas y Trasteros"),
    #                         ("capilla", "Capilla"),
    #                         ("sala_medios", "Sala de Medios"),
    #                         ("laboratorio", "Laboratorio"),
    #                         ("danza", "Danza"),
    #                     ]
    #                 elif obra_secundaria == "merced":
    #                     qcontext["estancia_options"] = [
    #                         ("eso_1_a", "1º ESO - A"),
    #                         ("eso_1_b", "1º ESO - B"),
    #                         ("eso_1_c", "1º ESO - C"),
    #                         ("eso_1_d", "1º ESO - D"),
    #                         ("eso_1_e", "1º ESO - E"),
    #                         ("eso_1_f", "1º ESO - F"),
    #                         ("eso_2_a", "2º ESO - A"),
    #                         ("eso_2_b", "2º ESO - B"),
    #                         ("eso_2_c", "2º ESO - C"),
    #                         ("eso_2_d", "2º ESO - D"),
    #                         ("eso_2_e", "2º ESO - E"),
    #                         ("eso_2_f", "2º ESO - F"),
    #                         ("eso_3_a", "3º ESO - A"),
    #                         ("eso_3_b", "3º ESO - B"),
    #                         ("eso_3_c", "3º ESO - C"),
    #                         ("eso_3_d", "3º ESO - D"),
    #                         ("eso_3_e", "3º ESO - E"),
    #                         ("eso_3_f", "3º ESO - F"),
    #                         ("eso_4_a", "4º ESO - A"),
    #                         ("eso_4_b", "4º ESO - B"),
    #                         ("eso_4_c", "4º ESO - C"),
    #                         ("eso_4_d", "4º ESO - D"),
    #                         ("eso_4_e", "4º ESO - E"),
    #                         ("eso_4_f", "4º ESO - F"),
    #                         ("bach_1_a", "1º Bachillerato - A"),
    #                         ("bach_1_b", "1º Bachillerato - B"),
    #                         ("bach_1_c", "1º Bachillerato - C"),
    #                         ("bach_1_d", "1º Bachillerato - D"),
    #                         ("bach_1_e", "1º Bachillerato - E"),
    #                         ("bach_2_a", "2º Bachillerato - A"),
    #                         ("bach_2_b", "2º Bachillerato - B"),
    #                         ("bach_2_c", "2º Bachillerato - C"),
    #                         ("bach_2_d", "2º Bachillerato - D"),
    #                         ("bach_2_e", "2º Bachillerato - E"),
    #                     ]
    #                 _logger.info(f"Qcontext final: {qcontext}")
    #                 return qcontext

    #     except Exception as e:
    #         _logger.error(f"Error en get_auth_signup_qcontext: {str(e)}")
    #     return {}

    # def _prepare_signup_values(self, qcontext):
    #     values = super()._prepare_signup_values(qcontext)

    #     def get_record_id(model, value):
    #         if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
    #             return int(value)
    #         record = request.env[model].sudo().search([("name", "=", value)], limit=1)
    #         return record.id if record else None

    #     if qcontext.get("estancia_id"):
    #         values["estancia_id"] = get_record_id(
    #             "res_partner", qcontext["estancia_id"]
    #         )
    #     if qcontext.get("obra_id"):
    #         values["obra_id"] = get_record_id("res_partner", qcontext["obra_id"])

    #     return values
