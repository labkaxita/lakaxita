define([
        'lakaxita/router', 
        ], function (Router) { 

    function App() {
        this.Router = Router;
        this.boot = function(options) {
            router = new this.Router(options);
            this.router = router;
            Backbone.View.prototype.reverse = function(route, subroute, model) { 
                return router.reverse(route, subroute, model);
            };
            Backbone.history.start();
        };
    };

    return App
});
