define([
        'lakaxita/utils/collections',
        'lakaxita/lost_found/models',
        ], function(Collections, LostFoundModels) {

    Items = Collections.Collection.extend({
        url: '/api/lost_items/',
        model: LostFoundModels.Item,
    });

    Notifications = Collections.Collection.extend({
        url: '/api/lost_item_notifications/',
    });

    return {Items: Items, Notifications: Notifications};
})
