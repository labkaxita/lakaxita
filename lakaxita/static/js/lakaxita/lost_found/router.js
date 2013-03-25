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
                view = new Views.ItemScroll({collection: items});
            items.fetch();
            this.renderScroll(view);
        },
        detail: function(slug) {
            var items = new Collections.Items();
            items.on('sync', function() {
                var model = items.findWhere({slug: slug}),
                    view = new Views.ItemDetail({model: model});
                this.renderContent(view);
            }, this);
            items.fetch();
        },
    });

    return Router;
})
