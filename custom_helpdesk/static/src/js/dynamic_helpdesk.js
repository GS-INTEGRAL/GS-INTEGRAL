odoo.define('custom_helpdesk.dynamic_fields', function (require) {
    'use strict';

    const ajax = require('web.ajax');

    // Escucha cambios en el campo obra_id
    $('#helpdesk_obra_id').on('change', function () {
        const obraId = $(this).val();

        if (obraId) {
            // Llamar al controlador para obtener estancias relacionadas
            ajax.jsonRpc('/get_estancias', 'call', { obra_id: obraId }).then(function (data) {
                const estanciaSelect = $('#helpdesk_estancia_id');
                estanciaSelect.empty();
                estanciaSelect.append('<option value="">Seleccione...</option>');
                data.forEach(estancia => {
                    estanciaSelect.append(`<option value="${estancia.id}">${estancia.name}</option>`);
                });
            });
        }
    });
});
