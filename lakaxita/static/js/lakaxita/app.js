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


    function App() {
        this.boot = function(container) {
            container = $(container);
            var router = new Router({'el': container});
            Backbone.history.start();
        };
        this.Router = Router;
        this.Views = Views;
        this.Collections = Collections;
    };

    return App
});
