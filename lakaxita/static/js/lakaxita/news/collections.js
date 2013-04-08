define([
        'backbone',
        'lakaxita/news/models',
        ], function(Backbone, Models) {

    News = Backbone.Collection.extend({
        url: '/api/news/',
        model: Models.News,
    });

    return {News: News};
})
