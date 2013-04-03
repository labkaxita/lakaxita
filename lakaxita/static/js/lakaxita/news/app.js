define([
        'lakaxita/utils/app',
        'lakaxita/news/collections', 
        'lakaxita/news/views', 
        ], function(App, Collections, Views) {

    scroll = new App.Scroll(Collections.News, Views.NewsScroll);
    detail = new App.Detail(Collections.News, Views.NewsDetail);
    return {scroll: scroll.run, detail: detail.run};
})
