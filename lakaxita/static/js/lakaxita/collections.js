(function() {
    Lakaxita.News = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/news/'
    });

    Lakaxita.Gallery = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/gallery/'
    });

    Lakaxita.Groups = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/groups/'
    });

    Lakaxita.LostItems = Backbone.Collection.extend({
        url: '/api/lost_found/',
        model: Backbone.Model.extend({
            title: function() { return this.get('name'); },
            date: function() { return this.get('lost'); },
            image: function() { return this.get('image'); },
            returned: function() { 
                if (this.get('returned')) {
                    return 'http://localhost:8000/static/admin/img/icon-yes.gif'; 
                } else {
                    return 'http://localhost:8000/static/admin/img/icon-no.gif';
                };
            },
        }),
    });

    Lakaxita.Attachments = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/attachments/'
    });
})()
