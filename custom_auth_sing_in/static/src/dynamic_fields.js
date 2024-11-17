odoo.define('custom_auth_sing_in.dynamic_fields', function (require) {
    'use strict';

    // Cuando obra_id cambia, actualiza las opciones de obra_ids
    $('#obra_id').on('change', function () {
        const obra_id = $(this).val();
        if (obra_id === 'maristas') {
            $.ajax({
                url: '/get_obra_options',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ obra_id }),
                success: function (response) {
                    const obraIdsSelect = $('#obra_ids');
                    obraIdsSelect.empty();
                    obraIdsSelect.append('<option value="">Seleccione...</option>');
                    response.forEach(option => {
                        obraIdsSelect.append(`<option value="${option.id}">${option.name}</option>`);
                    });
                    $('#obra_ids').parent().show();
                }
            });
        } else {
            $('#obra_ids').parent().hide();
        }
    });

    // Cuando obra_ids cambia, actualiza las opciones de estancias_id
    $('#obra_ids').on('change', function () {
        const obra_ids = $(this).val();
        $.ajax({
            url: '/get_estancias_options',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ obra_ids }),
            success: function (response) {
                const estanciasSelect = $('#estancias_id');
                estanciasSelect.empty();
                estanciasSelect.append('<option value="">Seleccione...</option>');
                response.forEach(option => {
                    estanciasSelect.append(`<option value="${option.id}">${option.name}</option>`);
                });
                $('#estancias_id').parent().show();
            }
        });
    });
});
