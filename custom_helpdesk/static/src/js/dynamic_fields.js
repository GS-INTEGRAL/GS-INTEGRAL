odoo.define('custom_helpdesk.dynamic_fields', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.DynamicFields = publicWidget.Widget.extend({
        selector: 'form', // El selector que engloba los campos (ajustar según la vista)
        events: {
            'change [name="company_id"]': '_onCompanyChange',
        },

        start: function () {
            this._super.apply(this, arguments);
            this._toggleFields(); // Inicializa los campos al cargar la página
        },

        _onCompanyChange: function () {
            this._toggleFields(); // Actualiza los campos cuando cambia company_id
        },

        _toggleFields: function () {
            const companyField = this.$('[name="company_id"]');
            const companyName = companyField.val();

            const maristasFields = this.$('.maristas-only');
            const noMaristasFields = this.$('.no-maristas');

            if (companyName === 'Maristas') {
                maristasFields.show();
                noMaristasFields.hide();
            } else {
                maristasFields.hide();
                noMaristasFields.show();
            }
        },
    });
});
