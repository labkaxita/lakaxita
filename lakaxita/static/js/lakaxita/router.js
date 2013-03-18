define(['lakaxita/views', 'lakaxita/collections'], function(Views, Collections) {

    Router = Backbone.Router.extend({
        initialize: function(options) {
            this.el = options.el;
        },
        render: function(view) {
            this.el.empty();
            this.el.append(view.render().el);
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
        index: function() {
            var view = new Views.Index();
            this.render(view);
        },
        lost_found: function() {
            var lost_items = new Collections.LostItems(),
                view = new Views.ItemList({collection: lost_items});
            lost_items.fetch();
            this.render(view);
        },
        lost_found_detail: function(slug) {
            var lost_items = new Collections.LostItems();
            lost_items.on('sync', function() {
                var model = lost_items.where({slug: slug})[0],
                    view = new Views.ItemDetail({model: model});
                this.render(view);
            }, this);
            lost_items.fetch();
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

    return Router;
})
