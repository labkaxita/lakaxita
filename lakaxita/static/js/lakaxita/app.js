define([
        'jquery', 
        'lakaxita/router', 
        ], function ($, Router) { 

    function App() {
        this.boot = function(container) {
            container = $(container);
            router = new Router({el: container});
            this.router = router;
            Backbone.View.prototype.reverse = function(route, subroute, model) { 
                return router.reverse(route, subroute, model);
            };
            Backbone.history.start();
        };
        this.Router = Router;
    };

    return App
});
