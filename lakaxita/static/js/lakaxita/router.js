define([
        'backbone',
        'underscore',
        'lakaxita/views',
        'lakaxita/lost_found/router',
        ], function(Backbone, _, Views, LostFoundRouter) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            this.el = options.el;
            this.$el = $(options.el);
            this.options = options;
            this.options['createTrailingSlashRoutes'] = true;
            this.subroutes = {
                lost_found: new LostFoundRouter('lost_found/', this.options),
            };
        },
        
        boot: function() {
            var view = new Views.Base();
            this.$el.html(view.render().el);
        },

        reverse: function(route, subroute, model) {
            var route = this.subroutes[route];
            var subroute = _.invert(route._routes)[subroute];
            var path = route.prefix + subroute;
            if (model) {
                path = path.replace(':slug', model.get('slug'));
            };
            path = '#' + path;
            return path;
        },
    });

    return Router;
})
