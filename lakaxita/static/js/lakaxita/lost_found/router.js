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
            var items = new Collections.Items(),
                view = new Views.ItemScroll({collection: items, el: this.scroll});
            items.fetch();
        },
        detail: function(slug) {
            var items = new Collections.Items(),
                view = new Views.ItemDetail({el: this.content});
            items.on('sync', function() {
                var model = items.findWhere({slug: slug});
                view.model = model;
                view.render();
            }, this);
            items.fetch();
        },
    });

    return Router;
})
