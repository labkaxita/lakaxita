define([
        'lakaxita/utils/views', 
        'lakaxita/news/collections',
        ], function(Views, Collections) {

    News = Views.View.extend({
        tagName: 'li',
        template: 'scroll_item',
        title: function() { return this.model.title(); },
        description: function() { return this.model.description(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.thumbnail(); },
        status: function() { return this.model.returned(); },
        url: function() { return this.reverse('lostFoundDetail', this.model); },
    });

    NewsScroll = Views.ScrollView.extend({
        className: 'news scroll',
        subView: News,
    });

    NewsDetail = News.extend({
        tagName: 'article',
        template: 'news/news_detail',
        image: function() { return this.model.image(); },
    });

    return {
        NewsScroll: NewsScroll,
        NewsDetail: NewsDetail,
    };
})
