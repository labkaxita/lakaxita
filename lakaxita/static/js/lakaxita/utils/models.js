define([
        'backbone.relational',
        'underscore',
        'lakaxita/errors',
        ], function(Backbone, _, Errors) {
 
    Model = Backbone.RelationalModel.extend({
        fetch: function(options) {
            options = options ? _.clone(options) : {};
            var error = options.error;
            options.error = function(model, response) {
                if (error) {
                    error(model, response);
                } else {
                    Errors.errorHandler(response);
                };
            };
            return Backbone.RelationalModel.prototype.fetch.apply(this, [options]);
        },
    });

    return {Model: Model};
});
