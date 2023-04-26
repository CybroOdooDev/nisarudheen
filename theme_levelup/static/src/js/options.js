odoo.define('theme_levelup.counter_option', function (require) {
'use strict';


    const options = require('web_editor.snippets.options');
    options.registry.CounterSnippet = options.Class.extend({
        selectDataAttribute: function (previewMode, widgetValue, params) {
            var val = parseInt(widgetValue);
            this.$target.attr("data-number", val);
        },
        _computeWidgetState: function (methodName, params) {
        alert(methodName)
        switch (methodName) {
            case 'selectDataAttribute': {
                return this.$target.find('.counter').attr('data-number');
            }
        }
        return this._super(...arguments);
    },
    });
});