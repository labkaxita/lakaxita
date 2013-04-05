define([], function() {

    View = function(view) {
        this.view = view;

        this.run = _.bind(function(options) {
            view = new this.view(options);
            return view;
        }, this);
    };

    Scroll = function(collection, view) {
        this.collection = collection;
        this.view = view;

        this.run = _.bind(function(options) {
            var collection = new this.collection(),
                view = new this.view({collection: collection, el: options.el});
            collection.fetch();
            return view;
        }, this);
    };

    Detail = function(collection, view) {
        this.collection = collection;
        this.view = view;

        this.run = _.bind(function(options) {
            var collection = new this.collection(),
                view = new this.view({el: options.el});
            collection.on('sync', function() {
                var model = collection.findWhere({slug: options.slug});
                view.model = model;
                view.render();
            });
            collection.fetch();
            return view;
        }, this);
    };
    
    return {Scroll: Scroll, Detail: Detail, View: View};
})
