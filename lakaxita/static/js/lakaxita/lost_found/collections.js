define(['backbone'], function(Backbone) {

    LostItems = Backbone.Collection.extend({
        url: '/api/lost_found/',
        model: Backbone.Model.extend({
            absolute_url: function() { return this.get('absolute_url'); },
            title: function() { return this.get('name'); },
            date: function() { return this.get('lost'); },
            image: function() { return this.get('image'); },
            thumbnail: function() { return this.get('thumbnail'); },
            returned: function() { 
                if (this.get('found') == null) {
                    return 'http://localhost:8000/static/admin/img/icon-no.gif';
                } else {
                    return 'http://localhost:8000/static/admin/img/icon-yes.gif'; 
                };
            },
        }),
    });

    return {LostItems: LostItems};
})
