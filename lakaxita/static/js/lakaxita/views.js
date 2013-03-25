define([
        'lakaxita/utils/views', 
        ], function(Views) {

    Base = Views.View.extend({
        tagName: 'body',
        template: 'base',
    });

    return {
        Base: Base,
    };
})
