define(['lib/backbone'], function(Backbone) {

    News = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/news/'
    });

    Gallery = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/gallery/'
    });

    Groups = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/groups/'
    });

    LostItems = Backbone.Collection.extend({
        url: '/api/lost_found/',
        model: Backbone.Model.extend({
            absolute_url: function() { return this.get('absolute_url'); },
            title: function() { return this.get('name'); },
            date: function() { return this.get('lost'); },
            image: function() { return this.get('image'); },
            thumbnail: function() { return this.get('thumbnail'); },
            returned: function() { 
                if (this.get('found') == null) {
                    return 'http://localhost:8000/static/admin/img/icon-yes.gif'; 
                } else {
                    return 'http://localhost:8000/static/admin/img/icon-no.gif';
                };
            },
        }),
    });

    Attachments = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/attachments/'
    });

    return {
        News: News,
        Gallery: Gallery,
        Groups: Groups,
        LostItems: LostItems,
        Attachments: Attachments,
    }
})
