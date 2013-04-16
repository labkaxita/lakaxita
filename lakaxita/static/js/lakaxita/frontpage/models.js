define([
        'backbone.relational',
        ], function(Backbone) {
 
    SiteDescription = Backbone.RelationalModel.extend({
        description: function() { return this.get('description'); },
        image: function() { return this.get('image'); },
        scaled_image: function() { return this.get('scaled_image'); },
    });

    return {SiteDescription: SiteDescription};

});
