define([
        'backbone',
        'jquery.kinetic',
        'underscore',
        'lakaxita/router', 
        ], function (Backbone, $, _, Router) { 

    function App() {
        this.Router = Router;

        this.boot = function(options) {
            this.options = options;
            this.setupErrorHandling();
            this.setupLoading();

            this.router = new this.Router(this.options);
            this.bindRouter(this.router);
            Backbone.history.start();

            this.setupMenu();
        };

        this.setupErrorHandling = function() {
            require.onError = function(error) {
                Backbone.trigger('lakaxita:error', error);
                throw error;
            };
        };

        this.bindRouter = function(router) {
            Backbone.View.prototype.router = router;
        };

        this.setupMenu = function() {
            $('*').live('click', _.bind(this.emptyMenu, this));
        };

        this.emptyMenu = function(event) {
            var menu = $(this.options.menu);
            if (this.router.navView.menuView && event.pageY < menu.offset().top) {
                this.router.navView.menuView.empty();
            };
        };

        this.setupLoading = function() {
            var loading = $('img#loading');
            $(document).ajaxStart(function() {
                loading.show();
            });
            $(document).ajaxStop(function() {
                loading.hide();
            });
        };
    };

    return App
});
