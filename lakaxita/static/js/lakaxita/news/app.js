define([
        'lakaxita/utils/app',
        'lakaxita/news/collections', 
        'lakaxita/news/views', 
        ], function(App, Collections, Views) {

    Scroll = new App.Scroll(Collections.News, Views.NewsScroll);
    Detail = new App.Detail(Collections.News, Views.NewsDetail);
    return {Scroll: Scroll.run, Detail: Detail.run};
})
