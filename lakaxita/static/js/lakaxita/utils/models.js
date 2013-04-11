define([
        'backbone.relational',
        'underscore',
        ], function(Backbone, _) {
 
    Model = Backbone.RelationalModel.extend({
        fetch: function(options) {
            options = options ? _.clone(options) : {};
            var error = options.error;
            options.error = function(model, response) {
                if (error) {
                    error(model, response);
                } else {
                    Backbone.trigger('lakaxita:error', response);
                };
            };
            return Backbone.RelationalModel.prototype.fetch.apply(this, [options]);
        },
    });

    return {Model: Model};
});
