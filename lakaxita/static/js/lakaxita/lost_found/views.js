define([
        'lakaxita/utils/views', 
        'lakaxita/lost_found/collections',
        ], function(Views, Collections) {

    Item = Views.View.extend({
        tagName: 'li',
        template: 'scroll_item',
        title: function() { return this.model.title(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.thumbnail(); },
        status: function() { return this.model.returned(); },
        url: function() { return this.reverse('lost_found', 'detail', this.model); },
    });

    ItemScroll = Views.ScrollView.extend({
        subView: Item,
    });

    ItemDetail = Item.extend({
        tagName: 'article',
        template: 'lost_found/item_detail',
        image: function() { return this.model.image(); },
        events: {'click button': 'notify'},
        notify: function(event) {
            event.preventDefault();
            var view = new ItemNotificationForm({
                collection: new Collections.Notifications(),
                item: this.model.id,
            });
            this.$el.append(view.render().el);
        },
    });

    ItemNotificationForm = Views.View.extend({
        initialize: function(options) {
            this.item = options.item;
            this.collection.on('add', this.success, this);
        },
        tagName: 'form',
        template: 'lost_found/notification_form',
        events: {'submit': 'submit'},
        submit: function(event) {
            event.preventDefault();
            this.collection.create({
                title: this.$('input#title').val(),
                reply_to: this.$('input#reply_to').val(),
                text: this.$('textarea#text').val(),
                item: this.item,
            });
        },
        success: function() { this.$el.empty(); },
    });

    return {
        ItemScroll: ItemScroll,
        ItemDetail: ItemDetail,
    };
})
