define([
        'jquery.kinetic',
        'underscore',
        'lakaxita/router', 
        ], function ($, _, Router) { 

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
            $('*').live('click', _.bind(this.emptyMenu, this))
        };

        this.emptyMenu = function(event) {
            var menu = $(this.options.menu);
            if (this.router.navView.menuView && event.pageY < menu.offset().top) {
                this.router.navView.menuView.empty();
            };
        };
    };

    return App
});
