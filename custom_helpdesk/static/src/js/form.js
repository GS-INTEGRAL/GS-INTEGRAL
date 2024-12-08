odoo.define('custom_helpdesk.form', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.CustomHelpdeskForm = publicWidget.Widget.extend({
        selector: '.custom_helpdesk_form',
        events: {
            'click .create_obra': '_onCreateObra',
            'click .create_estancia': '_onCreateEstancia',
        },

        /**
         * Método para manejar la creación de una nueva Obra/Sede.
         */
        _onCreateObra: function (ev) {
            ev.preventDefault();
            var self = this;
            var name = prompt("Ingrese el nombre de la nueva Obra/Sede:");
            if (name) {
                this._rpc({
                    route: '/custom_helpdesk/create_obra',
                    params: {
                        name: name,
                    },
                }).then(function (result) {
                    var select = self.$('#helpdesk_obra_secundaria');
                    select.append(new Option(result.name, result.id));
                    select.val(result.id);
                });
            }
        },

        /**
         * Método para manejar la creación de una nueva Estancia.
         */
        _onCreateEstancia: function (ev) {
            ev.preventDefault();
            var self = this;
            var name = prompt("Ingrese el nombre de la nueva Estancia:");
            if (name) {
                this._rpc({
                    route: '/custom_helpdesk/create_estancia',
                    params: {
                        name: name,
                    },
                }).then(function (result) {
                    var select = self.$('#helpdesk_estancia_id');
                    select.append(new Option(result.name, result.id));
                    select.val(result.id);
                });
            }
        },
    });
});
