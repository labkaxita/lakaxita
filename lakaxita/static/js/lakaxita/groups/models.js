define([
        'backbone.relational',
        ], function(Backbone) {
           
    Group = Backbone.RelationalModel.extend({
        name: function() { return this.get('name'); },
        description: function() { return this.get('description'); },
        image: function() { return this.get('image'); },
        scaled_image: function() { return this.get('scaled_image'); },
        stretched_image: function() { return this.get('stretched_image'); },
    });

    return {Group: Group};
});
