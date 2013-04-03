define([
        'backbone',
        'underscore',
        'jquery',
        'lakaxita/views',
        'lakaxita/lost_found/app',
        'lakaxita/news/app',
        ], function(Backbone, _, $, Views, LostFound, News) {

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
            'news/:slug/': 'newsDetail',
        },

        loadNav: function() {
            this.navView = new Views.Nav({el: this.nav, menu: this.menu});
        },

        lostFoundDetail: function(slug) {
            this.contentView = LostFound.detail(this.content, slug);
        },

        newsDetail: function(slug) {
            this.contentView = News.detail(this.content, slug);
        },
    });

    return Router;
})
