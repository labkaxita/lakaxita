define([
        'backbone',
        'jquery.kinetic',
        'underscore',
        'raven',
        'lakaxita/errors',
        'lakaxita/router', 
        ], function (Backbone, $, _, Raven, Errors, Router) { 

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
            require.onError = Errors.errorHandler;
            window.onerror = Errors.errorHandler;
        };

        this.bindRouter = function(router) {
            Backbone.View.prototype.router = router;
        };

        this.setupMenu = function() {
            $('*').live('click', _.bind(
                        this.router.navView.emptyMenuIfOutside, 
                        this.router.navView
                        ));
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
