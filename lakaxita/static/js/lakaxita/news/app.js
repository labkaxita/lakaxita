define([
        'lakaxita/utils/app',
        'lakaxita/news/collections', 
        'lakaxita/news/views', 
        ], function(App, Collections, Views) {

    Scroll = new App.generateScroll(Collections.News, Views.NewsScroll);
    Detail = new App.generateDetail(Collections.News, Views.NewsDetail);
    FrontpageScroll = new App.generateScroll(
        Collections.News, Views.FrontpageNewsScroll);

    return {
        Scroll: Scroll.run, 
        Detail: Detail.run, 
        FrontpageScroll: FrontpageScroll.run,
    };
})
