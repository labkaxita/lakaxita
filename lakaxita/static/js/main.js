require.config({
    baseUrl: '/static/js/',
    paths: {
        'text': 'lib/text',
        'handlebars': 'lib/handlebars',
        'underscore': 'lib/underscore',
        'backbone-tastypie': 'backbone-tastypie',
        'backbone': 'lib/backbone',
        'jquery': 'lib/jquery',
        'jquery.ui': 'lib/jquery.ui',
        'jquery.kinetic': 'lib/jquery.kinetic',
        'jquery.mousewheel': 'lib/jquery.mousewheel',
        'jquery.smoothdivscroll': 'lib/jquery.smoothdivscroll',
    },
    shim: {
        'handlebars': {
            exports: 'Handlebars',
        },
        'underscore': {
            exports: '_',
        },
        'jquery': {
            exports: '$',
        },
        'jquery.ui': {
            exports: '$',
            deps: ['jquery'],
        },
        'jquery.kinetic': {
            exports: '$',
            deps: ['jquery'],
        },
        'jquery.mousewheel': {
            exports: '$',
            deps: ['jquery'],
        },
        'jquery.smoothdivscroll': {
            exports: '$',
            deps: [
                'jquery', 
                'jquery.ui', 
                'jquery.mousewheel', 
                'jquery.kinetic',
            ],
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
        'jquery.smoothdivscroll',
        ], function(App) {

    Lakaxita = new App();
    window.Lakaxita = Lakaxita;
    Lakaxita.boot({
        content: 'section#content', 
        menu: 'section#menu',
        nav: 'section#nav',
    });
});
