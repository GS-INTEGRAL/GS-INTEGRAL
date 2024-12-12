odoo.define('custom_helpdesk.DynamicFields', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.DynamicFields = publicWidget.Widget.extend({
        selector: '#custom_fields_container',
        events: {
            'change #obras': '_onObrasChange',
        },

        start: function () {
            console.log('DynamicFields Widget has started'); // Confirmación de inicio
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                console.log('DynamicFields Widget initialization completed'); // Confirmación de finalización de inicialización
                self._updateFields();
            });
        },

        _updateFields: function () {
            console.log('Updating fields based on Maristas company');
            var isMaristas = this.$el.data('is-maristas');
            console.log('Is Maristas:', isMaristas); // Verificar si es de Maristas

            if (isMaristas) {
                this.$('.maristas-only').show();
                this.$('.no-maristas').hide();
                console.log('Showing Maristas-specific fields');
            } else {
                this.$('.maristas-only').hide();
                this.$('.no-maristas').show();
                console.log('Showing non-Maristas fields');
            }
        },

        _onObrasChange: function (ev) {
            var obra = $(ev.target).val();
            console.log('Obra selected:', obra); // Mostrar la obra seleccionada
            this._updateEstancias(obra);
        },

        _updateEstancias: function (obra) {
            console.log('Updating estancias for obra:', obra); // Mostrar la obra actual
            var $estancias = this.$('#estanciasid');
            $estancias.empty();

            // Agregar opciones dinámicamente con base en la obra seleccionada
            if (obra === 'fuensanta') {
                console.log('Adding estancias for Fuensanta');
                $estancias.append(new Option('Estancia Fuensanta 1', 'fuensanta_1'));
                $estancias.append(new Option('Estancia Fuensanta 2', 'fuensanta_2'));
            } else if (obra === 'merced') {
                console.log('Adding estancias for Merced');
                $estancias.append(new Option('Estancia Merced 1', 'merced_1'));
                $estancias.append(new Option('Estancia Merced 2', 'merced_2'));
            } else {
                console.log('No estancias available for selected obra');
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
