define([
        'lakaxita/utils/app',
        'lakaxita/nav/views', 
        ], function(App, Views) {

    Nav = new App.generateView(Views.Nav);
    NotFound = new App.generateView(Views.NotFound);

    return {Nav: Nav.run, NotFound: NotFound.run};
})
