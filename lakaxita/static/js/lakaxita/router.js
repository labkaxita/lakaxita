define([
        'backbone',
        'lakaxita/lost_found/router',
        ], function(Backbone, LostFoundRouter) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            this.options = options;
            this.options['createTrailingSlashRoutes'] = true;
            this.el = options.el;
            this.$el = $(options.el);
        },

        routes: {
            'lost_found(/*subroute)': 'invokeLostFound',
        },

        invokeLostFound: function(subroute) {
            if (!Router.LostFound) {
                Router.LostFound = new LostFoundRouter('lost_found/', this.options);
                };
        },
        groups: function() {
        },
        gallery: function() {
        },
        news: function() {
        },
        contact: function() {
        },
    });

    return Router;
})
