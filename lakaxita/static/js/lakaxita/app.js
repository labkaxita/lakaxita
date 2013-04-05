define([
        'lakaxita/router', 
        'jquery.kinetic',
        ], function (Router, $) { 

    function App() {
        this.Router = Router;

        this.boot = function(options) {
            this.setupScrolling(options.menu);

            router = new this.Router(options);
            this.router = router;

            Backbone.View.prototype.reverse = function(route, model) { 
                return router.reverse(route, model);
            };
            Backbone.history.start();
        };

        this.setupScrolling = function(el) {
            $(el).kinetic({cursor: 'ew-resize'});
        };
    };

    return App
});
