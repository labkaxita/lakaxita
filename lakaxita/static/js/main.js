require.config({
    baseUrl: '/static/js/',
    paths: {
        'text': 'lib/text',
        'handlebars': 'lib/handlebars',
        'underscore': 'lib/underscore',
        'backbone-tastypie': 'backbone-tastypie',
        'backbone': 'lib/backbone',
        'zen_coding': 'lib/zen_coding',
        'zen': 'lib/zen',
        'jquery': 'lib/jquery',
        'jquery.kinetic': 'lib/jquery.kinetic',
    },
    shim: {
        'handlebars': {
            exports: 'Handlebars',
        },
        'underscore': {
            exports: '_',
        },
        'zen': {
            exports: 'zen',
            deps: ['zen_coding', 'jquery'],
        },
        'jquery': {
            exports: '$',
        },
        'jquery.kinetic': {
            exports: '$',
            deps: ['jquery'],
        },
        'backbone-tastypie': {
            exports: 'Backbone',
            deps: ['backbone',],
        },
        'backbone': {
            exports: 'Backbone',
            deps: [
                'underscore',
                'handlebars', 
                'jquery',
            ],
        },
    },
});

define([
        'lakaxita/app', 
        'backbone-tastypie',
        ], function(App) {

    Lakaxita = new App();
    window.Lakaxita = Lakaxita;
    Lakaxita.boot({
        content: 'section#content', 
        menu: 'section#menu',
        nav: 'section#nav',
    });
});
