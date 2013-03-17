(function() {
    var Lakaxita = {};
    window.Lakaxita = Lakaxita;

    var template = function(name) {
        return Handlebars.compile($('#'+name+'-template').html());
    };

    Lakaxita.boot = function(container) {
        container = $(container);
        var router = new Lakaxita.Router({'el': container});
        Backbone.history.start();
    };

    Lakaxita.Router = Backbone.Router.extend({
        initialize: function(options) {
            this.el = options.el;
        },
        routes: {
            '': 'index',
            'lost_found': 'lost_found',
        },
        index: function() {
            var view = new Lakaxita.Index();
            this.el.empty();
            this.el.append(view.render());
        },
        lost_found: function() {
        },
    });

    Lakaxita.Index = Backbone.View.extend({
        template: template('index'),
        initialize: function() {
            this.news = new Lakaxita.News();
            this.news.on('all', this.render, this);
            this.news.fetch();
        },
        render: function() {
            return this.$el.html(this.template(this));
        },
    });

    Lakaxita.News = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/news/'
    });

    Lakaxita.Gallery = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/gallery/'
    });

    Lakaxita.Groups = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/groups/'
    });

    Lakaxita.LostItems = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/lost_found/'
    });

    Lakaxita.Attachments = Backbone.Collection.extend({
        model: Backbone.Model.extend(),
        url: '/api/attachments/'
    });
})()
