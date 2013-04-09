define([
        'backbone',
        'lakaxita/lost_found/models'
        ], function(Backbone, Models) {

    Items = Backbone.Collection.extend({
        url: '/api/lost_items/',
        model: Models.Item,
    });

    Notifications = Backbone.Collection.extend({
        url: '/api/lost_item_notifications/',
    });

    return {Items: Items, Notifications: Notifications};
})
