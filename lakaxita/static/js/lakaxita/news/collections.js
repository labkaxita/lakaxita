define(['backbone'], function(Backbone) {

    News = Backbone.Collection.extend({
        url: '/api/news/',
        model: Backbone.Model.extend({
            title: function() { return this.get('title'); },
            text: function() { return this.get('text'); },
            date: function() { return this.get('event'); },
            published: function() { return this.get('published'); },
            image: function() { return this.get('image'); },
            thumbnail: function() { return this.get('thumbnail'); },
            frontpage: function() { return this.get('frontpage'); },
            group: function() { return this.get('group'); },
        }),
    });

    return {News: News};
})
