define([
        'lakaxita/utils/app',
        'lakaxita/nav/views', 
        ], function(App, Views) {

    Nav = new App.generateView(Views.Nav);
    return {Nav: Nav.run};
})
