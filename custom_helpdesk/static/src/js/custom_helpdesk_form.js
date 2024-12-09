/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import FormEditorRegistry from "@website/js/form_editor_registry";

FormEditorRegistry.add('create_ticket', {
    formFields: [{
        type: 'char',
        required: true,
        name: 'partner_name',
        fillWith: 'name',
        string: _t('Your Name'),
    }, {
        type: 'email',
        required: true,
        name: 'partner_email',
        fillWith: 'email',
        string: _t('Your Email'),
    }, {
        type: 'char',
        modelRequired: true,
        name: 'name',
        string: _t('Subject'),
    }, {
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
    }, {
        type: 'text',
        name: 'description',
        string: _t('Description'),
    }, {
        type: 'binary',
        custom: true,
        name: _t('Attachment'),
    }],
    fields: [{
        name: 'team_id',
        type: 'many2one',
        relation: 'helpdesk.team',
        string: _t('Helpdesk Team'),
    }],
    successPage: '/your-ticket-has-been-submitted',
});
