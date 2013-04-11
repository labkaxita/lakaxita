define([
        'lakaxita/utils/collections',
        'lakaxita/news/models',
        ], function(Collections, NewsModels) {

    News = Collections.Collection.extend({
        url: '/api/news/',
        model: NewsModels.News,
    });

    return {News: News};
})
