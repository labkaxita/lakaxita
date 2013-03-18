define(['lakaxita/collections', 'lib/backbone'], function(Collections, Backbone) {

    /*__________HELPERS__________*/


    View = Backbone.View.extend({
        render: function() {
            /* FIXME there must be a better way */
            var view = this
            require(['text!'+this.template], function(template) {
                var template = Handlebars.compile(template);
                view.$el.html(template(view));
            });
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
        template: 'templates/index.html',
        initialize: function() {
            this.news = new Collections.News();
            this.news.fetch();
            this.news.on('sync', this.render, this);
        },
    });


    /*__________LOST_FOUND__________*/

    Item = View.extend({
        tagName: 'li',
        template: 'templates/item.html',
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
        template: 'templates/item_detail.html',
        image: function() { return this.model.image(); },
    });

    return {
        Index: Index,
        ItemList: ItemList,
        ItemDetail: ItemDetail,
    };
})
