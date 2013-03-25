define([
        'lakaxita/utils/views', 
        ], function(Views) {

    Nav = Views.View.extend({
        tagName: 'body',
        template: 'nav',
    });

    return {
        Nav: Nav,
    };
})
