define(['lakaxita/collections', 'lib/backbone'], function(Collections, Backbone) {

    /*__________HELPERS__________*/

    get_template = function(name) {
        return Handlebars.compile($('#'+name+'-template').html());
    };

    View = Backbone.View.extend({
        render: function() {
            this.$el.html(this.template(this));
            return this;
        },
    });

    CollectionView = Backbone.View.extend({
        tagName: 'ul',
        render: function(event) {
            this.$el.empty();
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                this.$el.append(view.render().el);
            }, this);
            return this;
        },
    });


    /*__________INDEX__________*/

    Index = View.extend({
        template: get_template('index'),
        initialize: function() {
            this.news = new Collections.News();
            this.news.fetch();
            this.news.on('sync', this.render, this);
        },
    });


    /*__________LOST_FOUND__________*/

    Item = View.extend({
        tagName: 'li',
        template: get_template('item'),
        title: function() { return this.model.title(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.thumbnail(); },
        status: function() { return this.model.returned(); },
        url: function() { return this.model.absolute_url(); },
    });

    ItemList = CollectionView.extend({
        subView: Item,
        initialize: function(options) {
            this.collection.on('sync', this.render, this);
        },
    });

    ItemDetail = Item.extend({
        tagName: 'article',
        template: get_template('item-detail'),
        image: function() { return this.model.image(); },
    });

    return {
        Index: Index,
        ItemList: ItemList,
        ItemDetail: ItemDetail,
    };
})
