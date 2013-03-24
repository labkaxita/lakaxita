require.config({
    baseUrl: '/static/js/',
    paths: {
        'text': 'lib/text',
        'handlebars': 'lib/handlebars',
        'underscore': 'lib/underscore',
        'jquery': 'lib/jquery',
        'backbone.subroute': 'lib/backbone.subroute',
        'backbone-tastypie': 'backbone-tastypie',
        'backbone': 'lib/backbone',
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
        'backbone.subroute': {
            exports: 'Backbone',
            deps: ['backbone'],
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

require(['lakaxita/app', 'backbone-tastypie'], function(App) {
    Lakaxita = new App();
    window.Lakaxita = Lakaxita;
    Lakaxita.boot('body');
});
