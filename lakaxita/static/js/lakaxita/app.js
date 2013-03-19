define([
        'jquery', 
        'lakaxita/router', 
        ], function (
            $, 
            Router
            ) { 


    function App() {
        this.boot = function(container) {
            container = $(container);
            var router = new Router({el: container});
            Backbone.history.start();
        };
        this.Router = Router;
    };

    return App
});
