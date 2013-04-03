define([
        'lakaxita/utils/app',
        'lakaxita/lost_found/collections', 
        'lakaxita/lost_found/views', 
        ], function(App, Collections, Views) {

    scroll = new App.Scroll(Collections.Items, Views.ItemScroll);
    detail = new App.Detail(Collections.Items, Views.ItemDetail);
    return {scroll: scroll.run, detail: detail.run};
})
