define([
        'backbone',
        'underscore',
        'jquery',
        'lakaxita/views',
        'lakaxita/lost_found/app',
        ], function(Backbone, _, $, Views, LostFound) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            options.createTrailingSlashRoutes = true;
            this.content = options.content;
            this.menu = options.menu;
            this.nav = options.nav;
            this.loadNav();
        },

        reverse: function(route, model) {
            var path = _.invert(this.routes)[route];
            if (model) {
                path = path.replace(':slug', model.get('slug'));
            };
            path = '#' + path;
            return path;
        },

        routes: {
            'lost_found/:slug/': 'lostFoundDetail',
        },

        loadNav: function() {
            this.navView = new Views.Nav({el: this.nav, menu: this.menu});
        },

        lostFoundDetail: function(slug) {
            this.contentView = LostFound.detail(this.content, slug);
        },
    });

    return Router;
})
