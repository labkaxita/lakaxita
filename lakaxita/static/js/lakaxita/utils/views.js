define([
        'backbone', 
        'zen',
        'lakaxita/utils/loading', 
        'text',
        ], function(Backbone, zen, Loading) {

    View = Backbone.View.extend({
        template_uri: function() {
            return 'text!/template/'+this.template+'/';
        },
        render: function() {
            Loading.show();
            var view = this;
            require([this.template_uri()], function(template) {
                var template = Handlebars.compile(template);
                view.$el.html(template(view));
            });
            Loading.hide();
            return this;
        },
    });

    ScrollView = Backbone.View.extend({
        list: 'ul.scroll',
        initialize: function(options) {
            if (! this.$list) {
                this.$list = zen(this.list);
            };
            this.$el.html(this.$list);
            this.$list.before(zen('div#left'));
            this.$list.after(zen('div#right'));
            this.collection.on('sync', this.render, this);
        },
        render: function() {
            Loading.show();
            this.$list.empty();
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                this.$list.append(view.render().el);
            }, this);
            Loading.hide();
            return this;
        },
        events: {
            'click li > a': 'empty',
            'click #left': 'scrollLeft',
            'click #right': 'scrollRight',
        },
        empty: function() {
            this.$el.empty();
        },
        scrollLeft: function() {
            this.$el.kinetic('start', {velocity: -10, decelerate: true});
        },
        scrollRight: function() {
            this.$el.kinetic('start', {velocity: 10, decelerate: true});
        },
    });

    return {
        View: View,
        ScrollView: ScrollView
    };
})
