define([
        'lakaxita/utils/views',
        'lakaxita/lost_found/app',
        'lakaxita/news/app',
        ], function(
            Views,
            LostFound,
            News
            ) {

    Nav = Views.View.extend({
        initialize: function(options) {
            this.options = options;
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
        },
        lostFound: function(event) {
            this.menuView = LostFound.Scroll({el: this.options.menu});
        },
        news: function(event) {
            this.menuView = News.Scroll({el: this.options.menu});
        },
    });

    return {Nav: Nav};
})
