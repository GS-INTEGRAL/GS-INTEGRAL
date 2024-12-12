odoo.define('custom_helpdesk.DynamicFields', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.DynamicFields = publicWidget.Widget.extend({
        selector: '#custom_fields_container',
        events: {
            'change #obras': '_onObrasChange',
        },

        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self._updateFields();
            });
        },

        _updateFields: function () {
            var isMaristas = this.$el.data('is-maristas');
            if (isMaristas) {
                this.$('.maristas-only').show();
                this.$('.no-maristas').hide();
            } else {
                this.$('.maristas-only').hide();
                this.$('.no-maristas').show();
            }
        },

        _onObrasChange: function (ev) {
            var obra = $(ev.target).val();
            this._updateEstancias(obra);
        },

        _updateEstancias: function (obra) {
            var $estancias = this.$('#estanciasid');
            $estancias.empty();

            // Aquí deberías agregar las opciones de estancias según la obra seleccionada
            // Este es solo un ejemplo, ajusta según tus necesidades
            if (obra === 'fuensanta') {
                $estancias.append(new Option('Estancia Fuensanta 1', 'fuensanta_1'));
                $estancias.append(new Option('Estancia Fuensanta 2', 'fuensanta_2'));
            } else if (obra === 'merced') {
                $estancias.append(new Option('Estancia Merced 1', 'merced_1'));
                $estancias.append(new Option('Estancia Merced 2', 'merced_2'));
            }
        }
    });
});


// odoo.define('custom_helpdesk.DynamicFields', function (require) {
//     'use strict';

//     const { Component } = owl;
//     const { useState } = owl.hooks;

//     class DynamicFields extends Component {
//         setup() {
//             this.state = useState({
//                 isMaristas: false, // Por defecto no es Maristas
//             });

//             // Actualizar estado según la compañía
//             const companyId = this.props.record.company_id || null;
//             if (companyId) {
//                 this.env.services.rpc({
//                     model: 'res.company',
//                     method: 'read',
//                     args: [[companyId], ['name']],
//                 }).then((company) => {
//                     if (company && company.length && company[0].name === 'Maristas') {
//                         this.state.isMaristas = true;
//                     }
//                 });
//             }
//         }
//     }

//     DynamicFields.template = 'custom_helpdesk.DynamicFields';
//     owl.Component.env = odoo.__DEBUG__.services;

//     return DynamicFields;
// });
