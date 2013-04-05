define([
        'lakaxita/utils/app',
        'lakaxita/news/collections', 
        'lakaxita/news/views', 
        ], function(App, Collections, Views) {

    Scroll = new App.generateScroll(Collections.News, Views.NewsScroll);
    Detail = new App.generateDetail(Collections.News, Views.NewsDetail);
    return {Scroll: Scroll.run, Detail: Detail.run};
})
