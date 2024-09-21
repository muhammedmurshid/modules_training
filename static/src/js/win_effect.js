odoo.define('module_training.win_effect', function (require) {
    'use strict';
    console.log('eeeee')

    var core = require('web.core');
    var Widget = require('web.Widget');

    var CelebrationButton = Widget.extend({
        events: {
            'click .celebrate-btn': '_onClickCelebrate',
        },

        _onClickCelebrate: function (ev) {
            ev.preventDefault();
            this._celebrate();
        },

        _celebrate: function () {
            // Confetti effect on button click
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        },
    });

    core.action_registry.add('celebration_button', CelebrationButton);
});