{
    "name": "Custom auth sing in",
    "version": "17.0.1.0.0",
    "summary": "Custom auth sing in",
    "description": "Campos en el sign in",
    "category": "Website",
    "author": "Pedo Mayor",
    "license": "LGPL-3",
    "depends": [
        "website",
        "base",
        "auth_signup",
        "website_helpdesk",
    ],
    "data": [
        # "views/auth_signup_login_inherit.xml",
        "views/view_partners_form_inherited.xml",
        "data/email_template_welcome.xml",
    ],
    # 'assets': {
    #     'web.assets_page': [
    #         '/custom_auth_sing_in/static/src/js/signup_custom.js',
    #     ],
    # },
    "installable": True,
    "application": False,
    "auto_install": False,
}
