define([
        'backbone',
        'lakaxita/frontpage/models',
        ], function(Backbone, Models) {

    SiteDescription = Backbone.Collection.extend({
        url: '/api/site_description/',
        model: Models.SiteDescription,
    });

    return {SiteDescription: SiteDescription};
})
