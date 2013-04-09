define([
        'backbone',
        'lakaxita/groups/models',
        ], function(Backbone, Models) {

    Groups = Backbone.Collection.extend({
        url: '/api/groups/',
        model: Models.Group,
    });

    return {Groups: Groups};
});
