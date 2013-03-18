define([
        'lib/jquery', 
        'lakaxita/router', 
        'lakaxita/views', 
        'lakaxita/collections',
        ], function (
            $, 
            Router,
            Views,
            Collections
            ) { 

    boot = function(container) {
        container = $(container);
        var router = new Router({'el': container});
        Backbone.history.start();
    };

    return {
        boot: boot,
        Router: Router,
        Views: Views,
        Collections: Collections,
    };
});
