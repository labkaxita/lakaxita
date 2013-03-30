define(['backbone.subroute', 'backbone', 'underscore'], function(subroute, Backbone, _) {

    SubRouter = Backbone.SubRoute.extend({
        constructor: function(prefix, options) {
            this._routes = _.clone(this.routes);
            Backbone.SubRoute.prototype.constructor.call(this, prefix, options);
        },
        initialize: function(options) {
            this.content = options.content;
            this.scroll = options.scroll;
        },
    });

    return {SubRouter: SubRouter};
})
