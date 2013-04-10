define([
        'lakaxita/utils/app',
        'lakaxita/frontpage/views', 
        ], function(App, Views) {

    Frontpage = new App.generateView(Views.Frontpage);
    return {Frontpage: Frontpage.run};
})
