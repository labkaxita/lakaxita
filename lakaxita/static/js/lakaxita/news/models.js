define([
        'lakaxita/utils/models',
        'lakaxita/groups/models',
        ], function(Models, GroupModels) {
           
    News = Models.Model.extend({
        title: function() { return this.get('title'); },
        text: function() { return this.get('text'); },
        event: function() { return this.get('event'); },
        published: function() { return this.get('published'); },
        image: function() { return this.get('image'); },
        thumbnail: function() { return this.get('thumbnail'); },
        frontpage: function() { return this.get('frontpage'); },
        attachments: function() { return this.get('attachments'); },
        group: function() { return this.get('group'); },

        relations: [{
            type: Backbone.HasOne,
            key: 'group',
            keyDestination: 'group',
            relatedModel: GroupModels.Group,
            autoFetch: true,
        }],
    });

    return {News: News};
});
