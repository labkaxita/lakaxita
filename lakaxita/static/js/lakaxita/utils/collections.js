define([
        'backbone.relational',
        'underscore',
        ], function(Backbone, _) {
 
    Collection = Backbone.Collection.extend({
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
            return Backbone.Collection.prototype.fetch.apply(this, [options]);
        },
    });

    return {Collection: Collection};
});
