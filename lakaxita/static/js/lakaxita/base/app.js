define([
        'lakaxita/utils/app',
        'lakaxita/base/views', 
        ], function(App, Views) {

    Nav = new App.View(Views.Nav);
    Frontpage = new App.View(Views.Frontpage);

    return {Nav: Nav.run, Frontpage: Frontpage.run};
})
