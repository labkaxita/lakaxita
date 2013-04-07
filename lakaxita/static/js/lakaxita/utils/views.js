define([
        'backbone', 
        'zen',
        'lakaxita/utils/loading', 
        'text',
        ], function(Backbone, zen, Loading) {

    View = Backbone.View.extend({
        getStatic: function(url) {
            return '/static/'+url;
        },
        getTemplate: function(url) {
            return '/template/'+this.template+'/';
        },
        getRequireTemplate: function(url) {
            return 'text!'+this.getTemplate(url);
        },
        render: function() {
            Loading.show();
            var view = this;
            require([this.getRequireTemplate(this.template)], function(template) {
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
