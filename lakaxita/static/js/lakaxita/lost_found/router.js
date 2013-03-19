define([
        'lakaxita/utils/routers',
        'lakaxita/lost_found/collections', 
        'lakaxita/lost_found/views', 
        ], function(Routers, Collections, Views) {

    Router = Routers.SubRouter.extend({
        routes: {
            '': 'scroll',
            ':slug/': 'detail',
        },
        scroll: function() {
            var lost_items = new Collections.LostItems(),
                view = new Views.ItemList({collection: lost_items});
            lost_items.fetch();
            this.renderScroll(view);
        },
        detail: function(slug) {
            var lost_items = new Collections.LostItems();
            lost_items.on('sync', function() {
                var model = lost_items.where({slug: slug})[0],
                    view = new Views.ItemDetail({model: model});
                this.renderContent(view);
            }, this);
            lost_items.fetch();
        },
    });

    return Router;
})
