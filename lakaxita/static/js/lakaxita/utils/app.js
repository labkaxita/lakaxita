define([], function() {


    Scroll = function(collection, view) {
        this.collection = collection;
        this.view = view;

        this.run = _.bind(function(el) {
            var collection = new this.collection(),
                view = new this.view({collection: collection, el:el});
            collection.fetch();
            return view;
        }, this);
    };

    Detail = function(collection, view) {
        this.collection = collection;
        this.view = view;

        this.run = _.bind(function(el, slug) {
            var collection = new this.collection(),
                view = new this.view({el: el});
            collection.on('sync', function() {
                var model = collection.findWhere({slug: slug});
                view.model = model;
                view.render();
            });
            collection.fetch();
            return view;
        }, this);
    };
    
    return {Scroll: Scroll, Detail: Detail};
})
