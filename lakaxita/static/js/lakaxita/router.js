define([
        'backbone',
        'underscore',
        'lakaxita/base/app',
        'lakaxita/lost_found/app',
        'lakaxita/news/app',
        ], function(Backbone, _, Base, LostFound, News) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            this.content = options.content;
            this.menu = options.menu;
            this.nav = options.nav;
            this.loadNav();
        },

        getReverse: function(route, model) {
            var path = _.invert(this.routes)[route];
            if (model) {
                path = path.replace(':slug', model.get('slug'));
            };
            path = '#' + path;
            return path;
        },

        routes: {
            '': 'frontpage',
            '/': 'frontpage',
            'lost_found/:slug/': 'lostFoundDetail',
            'news/:slug/': 'newsDetail',
        },

        loadNav: function() {
            this.navView = Base.Nav({el: this.nav, menu: this.menu});
        },

        frontpage: function() {
            this.contentView = Base.Frontpage({el: this.content});
        },

        lostFoundDetail: function(slug) {
            this.contentView = LostFound.Detail({el: this.content, slug: slug});
        },

        newsDetail: function(slug) {
            this.contentView = News.Detail({el: this.content, slug: slug});
        },
    });

    return Router;
})
