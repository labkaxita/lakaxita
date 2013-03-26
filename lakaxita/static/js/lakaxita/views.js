define([
        'lakaxita/utils/views', 
        ], function(Views) {

    Nav = Views.View.extend({
        tagName: 'body',
        template: 'nav',
        events: {
            'click ul#language > li > a': 'language',
        },
        language: function(event) {
            event.preventDefault();
            var lang = this.$(event.target).text();
            document.cookie = 'django_language='+lang;
            require.undef(this.template_uri());
            this.render();
        },
    });

    return {
        Nav: Nav,
    };
})
