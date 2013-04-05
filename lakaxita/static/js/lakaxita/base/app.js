define([
        'lakaxita/utils/app',
        'lakaxita/base/views', 
        ], function(App, Views) {

    Nav = new App.generateView(Views.Nav);
    Frontpage = new App.generateView(Views.Frontpage);

    return {Nav: Nav.run, Frontpage: Frontpage.run};
})
