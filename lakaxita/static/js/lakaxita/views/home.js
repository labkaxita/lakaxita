define(['lakaxita/collections', 'lakaxita/views/utils'], function(Collections, Views) {

    Index = Views.View.extend({
        template: 'templates/home.html',
        initialize: function() {
            this.news = new Collections.News();
            this.news.fetch();
            this.news.on('sync', this.render, this);
        },
    });

    return {
        Index: Index,
    };
})
