define([
        'lakaxita/utils/app',
        'lakaxita/base/views', 
        ], function(App, Views) {

    Nav = new App.View(Views.Nav);

    return {Nav: Nav.run};
})
