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
            'lost_found/:slug/': 'lost_found_detail',
            'groups': 'groups',
            'gallery': 'gallery',
            'news': 'news',
            'contact': 'contact',
        },
        render: function(view) {
            this.el.empty();
            this.el.append(view.render().el);
        },
        index: function() {
            var view = new Lakaxita.Index();
            this.render(view);
        },
        lost_found: function() {
            var lost_items = new Lakaxita.LostItems();
            lost_items.fetch();
            var view = new Lakaxita.ItemList({collection: lost_items});
            this.render(view);
        },
        lost_found_detail: function(slug) {
            var lost_items = new Lakaxita.LostItems();
            lost_items.fetch();
            var view = new Lakaxita.ItemDetail({collection: lost_items, slug: slug});
            this.render(view);
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
