define([
        'lakaxita/lost_found/collections', 
        'lakaxita/lost_found/views', 
        ], function(Collections, Views) {

    scroll = function(el) {
        var items = new Collections.Items(),
            view = new Views.ItemScroll({collection: items, el: el});
        items.fetch();
        return view;
    };

    detail = function(el, slug) {
        var items = new Collections.Items(),
            view = new Views.ItemDetail({el: el});
        items.on('sync', function() {
            var model = items.findWhere({slug: slug});
            view.model = model;
            view.render();
        });
        items.fetch();
        return view;
    };

    return {scroll: scroll, detail: detail};
})
