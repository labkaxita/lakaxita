define([
        'backbone',
        'underscore',
        'jquery',
        'lakaxita/views',
        'lakaxita/lost_found/router',
        ], function(Backbone, _, $, Views, LostFoundRouter) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            this.content = options.content;
            this.nav = options.nav;
            this.loadNav();

            var options = {
                el: this.content,
                createTrailingSlashRoutes: true,
            };
            this.subroutes = {
                lost_found: new LostFoundRouter('lost_found/', options),
            };
        },

        loadNav: function() {
            var view = new Views.Nav({el: $(this.nav)});
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
