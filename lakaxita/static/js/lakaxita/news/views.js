define([
        'lakaxita/utils/views', 
        'lakaxita/news/collections',
        ], function(Views, Collections) {

    News = Views.View.extend({
        tagName: 'li',
        template: 'scroll_item',
        title: function() { return this.model.title(); },
        text: function() { return this.model.text(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.thumbnail(); },
        status: function() { return this.model.group(); },
        url: function() { return this.reverse('newsDetail', this.model); },
    });

    NewsScroll = Views.ScrollView.extend({
        list: 'ul.scroll.news',
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
