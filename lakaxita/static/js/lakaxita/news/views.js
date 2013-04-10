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
            default_image: function() {
                return this.getStatic('imgs/scroll_news.svg');
            },
        },
    });

    NewsScroll = Views.ScrollView.extend({
        classReplacement: 'scroll news',
        subView: News,
    });

    FrontpageNewsScroll = NewsScroll.extend({
        classReplacement: 'scroll',
        data: {frontpage: true},
    });

    NewsDetail = News.extend({
        tagName: 'article',
        template: 'news/news_detail',
    });

    return {
        FrontpageNewsScroll: FrontpageNewsScroll,
        NewsScroll: NewsScroll,
        NewsDetail: NewsDetail,
    };
})
