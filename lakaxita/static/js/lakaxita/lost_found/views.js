define(['lakaxita/utils/views'], function(Views) {

    Item = Views.View.extend({
        tagName: 'li',
        template: 'templates/item.html',
        title: function() { return this.model.title(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.thumbnail(); },
        status: function() { return this.model.returned(); },
        url: function() { return this.model.absolute_url(); },
    });

    ItemList = Views.ScrollView.extend({
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
        ItemList: ItemList,
        ItemDetail: ItemDetail,
    };
})
