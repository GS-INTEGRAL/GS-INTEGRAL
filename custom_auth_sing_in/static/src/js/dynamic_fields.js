odoo.define('custom_auth_sign_in.dynamic_fields', function (require) {
    'use strict';

    // Cuando obra_id cambia
    $('#obra_id').on('change', function () {
        const obra_id = $(this).val();
        if (obra_id) {
            $.ajax({
                url: '/get_obra_ids_options',
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

    // Cuando obra_ids cambia
    $('#obra_ids').on('change', function () {
        const obra_ids = $(this).val();
        if (obra_ids) {
            $.ajax({
                url: '/get_estancia_options',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ obra_ids }),
                success: function (response) {
                    const estanciaSelect = $('#estancia_id');
                    estanciaSelect.empty();
                    estanciaSelect.append('<option value="">Seleccione...</option>');
                    response.forEach(option => {
                        estanciaSelect.append(`<option value="${option.id}">${option.name}</option>`);
                    });
                    $('#estancia_id').parent().show();
                }
            });
        } else {
            $('#estancia_id').parent().hide();
        }
    });
});
