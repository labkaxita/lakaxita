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
        renderPage: function(view) {
            this.$el.html(view.render().el);
        },
        renderContent: function(view) {
            var $el = this.$el.find('section#content');
            $el.html(view.render().el);
        },
        renderScroll: function(view) {
            var $el = this.$el.find('section#content');
            $el.find('ul.scroll').remove();
            $el.append(view.render().el);
        },
    });

    return {SubRouter: SubRouter};
})
