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
            require.undef(this.getRequireTemplate());
            this.render();
            if (this.menuView) {
                this.menuView.collection.fetch({prefill: true});
            };
        },
        lostFound: function(event) {
            this.menuView = LostFound.Scroll({el: this.menu});
        },
        news: function(event) {
            this.menuView = News.Scroll({el: this.menu});
        },
    });

    Frontpage = Backbone.View.extend({
        initialize: function(options) {
            this.news = zen('section#news');
            this.newsView = News.Scroll({el: this.news});
            this.$el.append(this.news);

            /* TODO: when gallery app ready
             * this.gallery = zen('section#gallery');
             * this.galleryView = Gallery.Scroll({el: this.gallery});
             * this.$el.append(this.gallery);
             * this.galleryView.collection.on(
             *                              'sync', 
             *                              this.galleryView.render, 
             *                              this.galleryView);
             */

            this.newsView.collection.on('sync', this.newsView.render, this.newsView);
        },
    });

    return {
        Nav: Nav,
        Frontpage: Frontpage,
    };
})
