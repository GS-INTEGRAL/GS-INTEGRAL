/** @odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { formEditorRegistry } from "@website/js/form_editor_registry.js";

const existingCreateTicket = formEditorRegistry.get('create_ticket');
formEditorRegistry.add('create_ticket', {
    ...existingCreateTicket,
    formFields: [
        ...existingCreateTicket.formFields,
        {
        type: 'char',
        name: 'obra_secundaria',
        string: _t('Sede/Obra'),
    }, {
        type: 'char',
        name: 'estancia_id',
        string: _t('Estancia'),
    }, {
        type: 'selection',
        name: 'categoria',
        string: _t('Categoría'),
        selection: [
            ['bricolage', 'Bricolaje'],
            ['fontaneria', 'Fontanería'],
            ['climatizacion', 'Climatización'],
            ['electricidad', 'Electricidad'],
            ['albañileria', 'Albañilería'],
            ['varios', 'Varios'],
            ['tic-ordenadores', 'Tic-Ordenadores'],
            ['mantenimiento', 'Mantenimiento'],
            ['pintura', 'Pintura'],
            ['herreria', 'Herrería'],
            ['jardineria', 'Jardinería'],
            ['carpinteria', 'Carpintería'],
            ['cristaleria', 'Cristalería'],
        ],
    }, 
],    
});
