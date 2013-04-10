define([
        'backbone.relational',
        ], function(Backbone) {
 
    SiteDescription = Backbone.RelationalModel.extend({
        description: function() { return this.get('description'); },
        image: function() { return this.get('image'); },
        thumbnail: function() { return this.get('thumbnail'); },
    });

    return {SiteDescription: SiteDescription};

});
