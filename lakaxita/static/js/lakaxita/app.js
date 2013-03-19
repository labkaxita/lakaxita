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
            Backbone.history.start();
            var router = new Router({el: container});
        };
        this.Router = Router;
    };

    return App
});
