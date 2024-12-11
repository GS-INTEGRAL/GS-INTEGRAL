odoo.define('custom_helpdesk.DynamicFields', function (require) {
    'use strict';

    const { Component } = owl;
    const { useState } = owl.hooks;

    class DynamicFields extends Component {
        setup() {
            this.state = useState({
                isMaristas: false, // Por defecto no es Maristas
            });

            // Actualizar estado según la compañía
            const companyId = this.props.record.company_id || null;
            if (companyId) {
                this.env.services.rpc({
                    model: 'res.company',
                    method: 'read',
                    args: [[companyId], ['name']],
                }).then((company) => {
                    if (company && company.length && company[0].name === 'Maristas') {
                        this.state.isMaristas = true;
                    }
                });
            }
        }
    }

    DynamicFields.template = 'custom_helpdesk.DynamicFields';
    owl.Component.env = odoo.__DEBUG__.services;

    return DynamicFields;
});
