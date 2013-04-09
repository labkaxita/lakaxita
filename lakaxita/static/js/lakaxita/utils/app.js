define([], function() {

    generateView = function(view) {
        this.view = view;

        this.run = _.bind(function(options) {
            view = new this.view(options);
            return view;
        }, this);
    };

    generateScroll = function(collection, view) {
        this.collection = collection;
        this.view = view;

        this.run = _.bind(function(options) {
            var collection = new this.collection(),
                view = new this.view({collection: collection, el: options.el});
            collection.fetch({prefill: true, data: view.data});
            return view;
        }, this);
    };

    generateDetail = function(collection, view) {
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
            collection.fetch({prefill: true, data: view.data});
            return view;
        }, this);
    };
    
    return {
        generateView: generateView,
        generateScroll: generateScroll,
        generateDetail: generateDetail,
    };
})
