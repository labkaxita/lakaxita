define([
        'lakaxita/utils/views', 
        'lakaxita/lost_found/app',
        ], function(
            Views,
            LostFound
            ) {

    Nav = Views.View.extend({
        initialize: function(options) {
            this.menu = options.menu;
        },
        tagName: 'body',
        template: 'nav',
        events: {
            'click ul#language > li > a': 'language',

            'click nav .lost-found > a': 'lostFound',
        },
        language: function(event) {
            event.preventDefault();
            var lang = this.$(event.target).text();
            document.cookie = 'django_language='+lang;
            require.undef(this.template_uri());
            this.render();
        },
        lostFound: function(event) {
            this.menuView = LostFound.scroll(this.menu);
        },
    });

    return {
        Nav: Nav,
    };
})
