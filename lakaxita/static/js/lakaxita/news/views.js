define([
        'lakaxita/utils/views', 
        'lakaxita/news/collections',
        ], function(Views, Collections) {

    News = Views.View.extend({
        tagName: 'li',
        template: 'scroll_item',
        extraContext: {
            hover: function() { return this.model.published(); },
            icon: function() { 
                var group = this.model.group();
                if (group) {
                    return group.image();
                };
            },
            url: function() { 
                return this.router.getReverse('newsDetail', this.model);
            },
        },
    });

    NewsScroll = Views.ScrollView.extend({
        className: 'news',
        subView: News,
    });

    NewsDetail = News.extend({
        tagName: 'article',
        template: 'news/news_detail',
    });

    return {
        NewsScroll: NewsScroll,
        NewsDetail: NewsDetail,
    };
})
