define(['backbone'], function(Backbone) {

    Items = Backbone.Collection.extend({
        url: '/api/lost_items/',
        model: Backbone.Model.extend({
            absolute_url: function() { return this.get('absolute_url'); },
            title: function() { return this.get('name'); },
            date: function() { return this.get('lost'); },
            image: function() { return this.get('image'); },
            thumbnail: function() { return this.get('thumbnail'); },
            returned: function() { 
                if (this.get('found') == null) {
                    return 'http://localhost:8000/static/admin/img/icon-no.gif';
                } else {
                    return 'http://localhost:8000/static/admin/img/icon-yes.gif'; 
                };
            },
        }),
    });

    Notifications = Backbone.Collection.extend({
        url: '/api/lost_item_notifications/',
    });

    return {Items: Items, Notifications: Notifications};
})
