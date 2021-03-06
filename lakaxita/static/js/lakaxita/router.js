define([
        'backbone',
        'underscore',
        'lakaxita/nav/app',
        'lakaxita/frontpage/app',
        'lakaxita/lost_found/app',
        'lakaxita/news/app',
        ], function(Backbone, _, Nav, Frontpage, LostFound, News) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            this.options = options;
            this.loadNav();
        },

        getReverse: function(route, model) {
            var path = _.invert(this.routes)[route];
            if (model) {
                path = path.replace(':slug', model.get('slug'));
            };
            path = '#/' + path;
            return path;
        },

        routes: {
            '': 'frontpage',
            '/': 'frontpage',
            'lost_found/:slug/': 'lostFoundDetail',
            'news/:slug/': 'newsDetail',
            '*path': 'notFound',
        },

        loadNav: function() {
            this.navView = Nav.Nav({
                el: this.options.nav, 
                menu: this.options.menu,
            });
        },

        frontpage: function() {
            this.contentView = Frontpage.Frontpage({el: this.options.content});
        },

        lostFoundDetail: function(slug) {
            this.contentView = LostFound.Detail({
                el: this.options.content, 
                slug: slug,
            });
        },

        newsDetail: function(slug) {
            this.contentView = News.Detail({
                el: this.options.content, 
                slug: slug,
            });
        },

        notFound: function(path) {
            this.contentView = Nav.NotFound({
                el: this.options.content,
                path: path,
            });
            this.contentView.render();
        },
    });

    return Router;
})
