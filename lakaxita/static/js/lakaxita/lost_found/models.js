define([
        'lakaxita/utils/models',
        ], function(Models) {

    Item = Models.Model.extend({
        title: function() { return this.get('name'); },
        description: function() { return this.get('description'); },
        date: function() { return this.get('lost'); },
        image: function() { return this.get('image'); },
        scaled_image: function() { return this.get('scaled_image'); },
        stretched_image: function() { return this.get('stretched_image'); },
        returned: function() { return this.get('found') == null; },
    });

    return {Item: Item};
})
