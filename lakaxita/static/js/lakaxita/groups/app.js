define([
        'lakaxita/utils/app',
        'lakaxita/groups/collections', 
        'lakaxita/groups/views', 
        ], function(App, Collections, Views) {

    Scroll = new App.generateScroll(Collections.Groups, Views.GroupScroll);
    Detail = new App.generateDetail(Collections.Groups, Views.GroupDetail);
    return {Scroll: Scroll.run, Detail: Detail.run};
})
