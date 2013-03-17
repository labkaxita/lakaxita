(function() {
    var Lakaxita = {};
    window.Lakaxita = Lakaxita;

    Lakaxita.get_template = function(name) {
        return Handlebars.compile($('#'+name+'-template').html());
    };

    Lakaxita.boot = function(container) {
        container = $(container);
        var router = new Lakaxita.Router({'el': container});
        Backbone.history.start();
    };

    Lakaxita.Router = Backbone.Router.extend({
        initialize: function(options) {
            this.el = options.el;
        },
        routes: {
            '': 'index',
            'lost_found': 'lost_found',
            'groups': 'groups',
            'gallery': 'gallery',
            'news': 'news',
            'contact': 'contact',
        },
        index: function() {
            var view = new Lakaxita.Index();
            this.el.empty();
            this.el.append(view.render().el);
        },
        lost_found: function() {
            var lost_items = new Lakaxita.LostItems();
            var view = new Lakaxita.ItemList({collection: lost_items});
            this.el.append(view.render().el);
        },
        groups: function() {
            this.el.empty();
        },
        gallery: function() {
            this.el.empty();
        },
        news: function() {
            this.el.empty();
        },
        contact: function() {
            this.el.empty();
        },
    });
})()
