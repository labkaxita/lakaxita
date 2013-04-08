define(['backbone'], function(Backbone) {

    Item = Backbone.Model.extend({
        title: function() { return this.get('name'); },
        description: function() { return this.get('description'); },
        date: function() { return this.get('lost'); },
        image: function() { return this.get('image'); },
        thumbnail: function() { return this.get('thumbnail'); },
        returned: function() { return this.get('found') == null; },
    });

    return {Item: Item};
})
