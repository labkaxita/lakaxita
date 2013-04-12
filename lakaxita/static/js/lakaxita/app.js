define([
        'backbone',
        'jquery.kinetic',
        'underscore',
        'raven',
        'lakaxita/router', 
        ], function (Backbone, $, _, Raven, Router) { 

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
            Raven.config([
                    'https://8be3d66e72604e20bb74712f39926d69:',
                    '186dc82c9a4749129a9b9652cde82390@',
                    'app.getsentry.com/4320',
                    ].join('')).install();

            errorHandler = function(error) {
                Raven.captureException(error);
                alert([
                        'Houston we\'ve had a problem.',
                        'We\'ve had a MAIN B BUS UNDERVOLT.',
                        'Roger. MAIN B UNDERVOLT.',
                        'Okay, stand by, 13. We\'re looking at it.',
                        ].join('\n'));
                throw error;
            };
            require.onError = errorHandler;
            window.onerror = errorHandler;
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
