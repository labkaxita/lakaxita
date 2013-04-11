require.config({
    catchError: true,
    baseUrl: '/static/js/',
    paths: {
        'text': 'lib/text',
        'raven': 'lib/raven',
        'handlebars': 'lib/handlebars',
        'underscore': 'lib/underscore',
        'backbone-tastypie': 'backbone-tastypie',
        'backbone.relational': 'lib/backbone.relational',
        'backbone.fetch-cache': 'lib/backbone.fetch-cache',
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
        'backbone.relational': {
            exports: 'Backbone',
            deps: [
                'backbone-tastypie', 
                'backbone.fetch-cache',
                'backbone',
                ],
        },
        'backbone-tastypie': {
            exports: 'Backbone',
            deps: ['backbone',],
        },
        'backbone.fetch-cache': {
            exports: 'Backbone',
            deps: ['backbone'],
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
        'backbone.relational',
        ], function(App) {

    Lakaxita = new App();
    window.Lakaxita = Lakaxita;
    Lakaxita.boot({
        content: 'section#content', 
        menu: 'section#menu',
        nav: 'section#nav',
    });
});
