require.config({
    baseUrl: '/static/js/',
    paths: {
        'text': 'lib/text'
    },
    shim: {
        'lib/handlebars': {
            exports: 'Handlebars',
        },
        'lib/underscore': {
            exports: '_',
        },
        'lib/jquery': {
            exports: '$',
        },
        'backbone-tastypie': {
            exports: 'Backbone',
            deps: ['lib/backbone'],
        },
        'lib/backbone': {
            exports: 'Backbone',
            deps: [
                'lib/underscore',
                'lib/handlebars', 
                'lib/jquery',
            ],
        },
    },
});

define(['lakaxita/app', 'backbone-tastypie'], function(Lakaxita) {
    window.Lakaxita = Lakaxita
    Lakaxita.boot('section#content');
});
