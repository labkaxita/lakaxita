define([
        'lakaxita/utils/views', 
        ], function(Views) {

    Base = Views.View.extend({
        tagName: 'div',
        template: 'base.html',
    });

    return {
        Base: Base,
    };
})
