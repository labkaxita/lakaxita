define([
        'lakaxita/router', 
        'jquery.smoothdivscroll',
        ], function (Router, $) { 

    function App() {
        this.Router = Router;

        this.boot = function(options) {
            this.setupScrolling(options.scroll);

            router = new this.Router(options);
            this.router = router;

            Backbone.View.prototype.reverse = function(route, subroute, model) { 
                return router.reverse(route, subroute, model);
            };
            Backbone.history.start();
        };

        this.setupScrolling = function(el) {
            $(el).parent().kinetic();
        };
    };

    return App
});
