define(['backbone'], function(Backbone) {

    Items = Backbone.Collection.extend({
        url: '/api/lost_items/',
        model: Backbone.Model.extend({
            title: function() { return this.get('name'); },
            description: function() { return this.get('description'); },
            date: function() { return this.get('lost'); },
            image: function() { return this.get('image'); },
            thumbnail: function() { return this.get('thumbnail'); },
            returned: function() { return this.get('found') == null; },
        }),
    });

    Notifications = Backbone.Collection.extend({
        url: '/api/lost_item_notifications/',
    });

    return {Items: Items, Notifications: Notifications};
})
