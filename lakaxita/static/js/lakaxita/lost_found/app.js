define([
        'lakaxita/utils/app',
        'lakaxita/lost_found/collections', 
        'lakaxita/lost_found/views', 
        ], function(App, Collections, Views) {

    Scroll = new App.Scroll(Collections.Items, Views.ItemScroll);
    Detail = new App.Detail(Collections.Items, Views.ItemDetail);
    return {Scroll: Scroll.run, Detail: Detail.run};
})
