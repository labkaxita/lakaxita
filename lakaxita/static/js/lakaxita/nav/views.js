define([
        'backbone',
        'lakaxita/utils/views',
        'lakaxita/lost_found/app',
        'lakaxita/news/app',
        ], function(
            Backbone,
            Views,
            LostFound,
            News
            ) {

    Nav = Views.View.extend({
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
            Backbone.history.location.reload();
        },
        lostFound: function(event) {
            this.menuView = LostFound.Scroll({el: this.options.menu});
        },
        news: function(event) {
            this.menuView = News.Scroll({el: this.options.menu});
        },
        emptyMenuIfOutside: function(event) {
            var menu = $(this.options.menu);
            if (this.menuView && event.pageY < menu.offset().top) {
                this.menuView.empty();
            };
        },
    });

    NotFound = Views.View.extend({
        template: '404',
    });
    return {Nav: Nav, NotFound: NotFound};
})
