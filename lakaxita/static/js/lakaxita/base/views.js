define([
        'backbone',
        'zen',
        'lakaxita/utils/views',
        'lakaxita/lost_found/app',
        'lakaxita/news/app',
        ], function(
            Backbone,
            zen,
            Views,
            LostFound,
            News
            ) {

    Nav = Views.View.extend({
        initialize: function(options) {
            this.menu = options.menu;
        },
        template: 'nav',
        events: {
            'click ul#language > li > a': 'language',

            'click nav .lost-found > a': 'lostFound',
            'click nav .news > a': 'news',
        },
        language: function(event) {
            event.preventDefault();
            var lang = this.$(event.target).text();
            document.cookie = 'django_language='+lang;
            require.undef(this.template_uri());
            this.render();
            if (this.menuView) {
                this.menuView.collection.fetch();
            };
        },
        lostFound: function(event) {
            this.menuView = LostFound.Scroll({el: this.menu});
        },
        news: function(event) {
            this.menuView = News.Scroll({el: this.menu});
        },
    });

    return {
        Nav: Nav,
    };
})
