odoo.define('module_training.win_effect_trigger', function (require) {
    'use strict';
     console.log('eeeee')

    const AbstractAction = require('web.AbstractAction');
    const core = require('web.core');
    const winEffect = require('module_training.win_effect');

    const WinEffectAction = AbstractAction.extend({
        start: function () {
            this._super.apply(this, arguments);
            winEffect.startConfettiEffect();  // Call your custom effect function
        },
    });

    // Register the custom client action
    core.action_registry.add('trigger_win_effect', WinEffectAction);
});
