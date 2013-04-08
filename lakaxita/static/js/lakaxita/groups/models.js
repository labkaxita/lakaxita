define([
        'backbone.relational',
        ], function(Backbone) {
           
    Group = Backbone.RelationalModel.extend({
        name: function() { return this.get('name'); },
        description: function() { return this.get('description'); },
        image: function() { return this.get('image'); },
        thumbnail: function() { return this.get('thumbnail'); },
    });

    return {Group: Group};
});
