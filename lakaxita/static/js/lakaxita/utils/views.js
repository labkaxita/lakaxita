define([
        'backbone', 
        'underscore',
        'zen',
        'lakaxita/utils/loading', 
        'text',
        ], function(Backbone, _, zen, Loading) {

    View = Backbone.View.extend({
        data: {},
        getContext: function() {
            var context = _.extend(this.model);
            console.log(context)
            var extraContext = _.extend(this.extraContext);
            view = this;
            _.each(_.functions(extraContext), function(name) {
                func = _.bind(extraContext[name], view);
                context[name] = func;
            });
            return context;
        },
        getStatic: function(url) {
            return '/static/'+url;
        },
        getTemplate: function(url) {
            return '/template/'+this.template+'/';
        },
        getRequireTemplate: function(url) {
            return 'text!'+this.getTemplate(url);
        },
        loadTemplate: function(callback) {
            require([this.getRequireTemplate(this.template)], function(template) {
                var template = Handlebars.compile(template);
                return callback(template);
            });
        },
        render: function() {
            Loading.show();
            this.loadTemplate(_.bind(function(template) {
                var rendered = template(this.getContext());
                this.$el.html(rendered);
            }, this));
            Loading.hide();
            return this;
        },
    });

    ScrollView = View.extend({
        template: 'scroll',
        initialize: function(options) {
            this.collection.on('sync', this.render, this);
        },
        render: function() {
            Loading.show();

            var subview_elements = [];
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                element = view.render().$el;
                subview_elements.push(element);
            }, this);

            this.loadTemplate(_.bind(function(template) {
                var rendered = template({subviews: subview_elements});
                this.$el.html(rendered);
            }, this));

            if (this.classReplacement) {
                this.$el.removeClass().addClass(this.classReplacement);
            };

            Loading.hide();
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
