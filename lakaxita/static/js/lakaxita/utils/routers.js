define(['backbone.subroute', 'backbone'], function(subroute, Backbone) {

    SubRouter = Backbone.SubRoute.extend({
        initialize: function(options) {
            this.el = options.el;
            this.$el = $(options.el);
        },
        renderContent: function(view) {
            this.el.html(view.render().el);
        },
        renderScroll: function(view) {
            this.$el.find('ul.scroll').remove();
            this.el.append(view.render().el);
        },
    });

    return {SubRouter: SubRouter};
})
