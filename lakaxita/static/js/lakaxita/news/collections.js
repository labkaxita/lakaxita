define(['backbone'], function(Backbone) {

    News = Backbone.Collection.extend({
        url: '/api/news/',
        model: Backbone.Model.extend({
            title: function() { return this.get('name'); },
            description: function() { return this.get('description'); },
            date: function() { return this.get('lost'); },
            image: function() { return this.get('image'); },
            thumbnail: function() { return this.get('thumbnail'); },
            returned: function() { return this.get('found') == null; },
        }),
    });

    return {News: News};
})
