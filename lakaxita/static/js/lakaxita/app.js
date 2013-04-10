define([
        'jquery.kinetic',
        'lakaxita/router', 
        ], function ($, Router) { 

    function App() {
        this.Router = Router;

        this.boot = function(options) {
            this.options = options;
            this.setupScrolling(this.options.menu);
            this.router = new this.Router(this.options);
            this.bindRouter();
            Backbone.history.start();
        };

        this.bindRouter = function() {
            Backbone.View.prototype.router = this.router;
        };

        this.setupScrolling = function(el) {
            $(el).kinetic({cursor: 'ew-resize'});
        };
    };

    return App
});
