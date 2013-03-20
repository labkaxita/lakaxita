define(['backbone.subroute', 'backbone', 'underscore'], function(subroute, Backbone, _) {

    SubRouter = Backbone.SubRoute.extend({
        constructor: function(prefix, options) {
            this._routes = _.clone(this.routes);
            Backbone.SubRoute.prototype.constructor.call(this, prefix, options);
        },
        initialize: function(options) {
            this.el = options.el;
            this.$el = $(options.el);
        },
        renderContent: function(view) {
            this.el.html(view.render().el);
        },
        renderScroll: function(view) {
            this.$el.find('ul.scroll').remove();
            this.$el.append(view.render().el);
        },
    });

    return {SubRouter: SubRouter};
})
