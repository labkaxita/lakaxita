define([
        'lakaxita/utils/app',
        'lakaxita/base/nav', 
        'lakaxita/base/frontpage', 
        ], function(App, NavView, FrontpageView) {

    Nav = new App.generateView(NavView);
    Frontpage = new App.generateView(FrontpageView);

    return {Nav: Nav.run, Frontpage: Frontpage.run};
})
