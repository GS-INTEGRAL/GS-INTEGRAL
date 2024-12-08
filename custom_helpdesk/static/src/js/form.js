odoo.define('custom_helpdesk.form', function (require) {
    "use strict";

    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var registry = require('web.registry');
    var { Component } = owl;

    class UploadProgressToast extends Component {}
    UploadProgressToast.template = "web_editor.UploadProgressToast";

    registry.category("components").add("UploadProgressToast", UploadProgressToast);

    publicWidget.registry.CustomHelpdeskForm = publicWidget.Widget.extend({
        selector: '.custom_helpdesk_form',
        events: {
            'click .create_obra': '_onCreateObra',
            'click .create_estancia': '_onCreateEstancia',
        },

        start: function () {
            this.uploadProgressToast = new UploadProgressToast();
            return this._super.apply(this, arguments);
        },

        _onCreateObra: function (ev) {
            // ... código existente ...
        },

        _onCreateEstancia: function (ev) {
            // ... código existente ...
        },
    });
});
