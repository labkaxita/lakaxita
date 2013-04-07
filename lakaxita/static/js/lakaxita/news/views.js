define([
        'lakaxita/utils/views', 
        'lakaxita/news/collections',
        ], function(Views, Collections) {

    News = Views.View.extend({
        tagName: 'li',
        template: 'scroll_item',
        title: function() { return this.model.title(); },
        text: function() { return this.model.text(); },
        event: function() { return this.model.event(); },
        published: function() { return this.model.published(); },
        image: function() { return this.model.thumbnail(); },
        group: function() { return this.model.group(); },
        status: function() { return this.model.group(); },
        hover: function() { return this.model.date(); },
        url: function() { 
            return this.router.getReverse('newsDetail', this.model);
        },
    });

    NewsScroll = Views.ScrollView.extend({
        className: 'news',
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
