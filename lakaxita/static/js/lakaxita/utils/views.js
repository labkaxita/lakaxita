define([
        'backbone', 
        'underscore',
        'zen',
        'jquery.kinetic',
        'text',
        ], function(Backbone, _, zen, $) {

    View = Backbone.View.extend({
        initialize: function(options) {
            this.options = options;
        },
        data: {},
        getContext: function() {
            var context = _.extend(this.model);
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
            this.loadTemplate(_.bind(function(template) {
                var rendered = template(this.getContext());
                this.$el.html(rendered);
            }, this));
            return this;
        },
    });

    ScrollView = View.extend({
        template: 'scroll',
        render: function() {
            var subview_elements = [];
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                element = view.render().$el;
                subview_elements.push(element);
            }, this);

            this.loadTemplate(_.bind(function(template) {
                var rendered = template({subviews: subview_elements});
                this.$el.html(rendered);
                this.$('.kinetic').kinetic({cursor: 'ew-resize'});
            }, this));

            if (this.classReplacement) {
                this.$el.removeClass().addClass(this.classReplacement);
            };

            return this;
        },
        events: {
            'click li > a': 'empty',
            'click .left': 'scrollLeft',
            'click .right': 'scrollRight',
        },
        empty: function() {
            this.$el.empty();
        },
        scrollLeft: function() {
            this.$('.kinetic').kinetic('start', {velocity: -10, decelerate: true});
        },
        scrollRight: function() {
            this.$('.kinetic').kinetic('start', {velocity: 10, decelerate: true});
        },
    });

    return {
        View: View,
        ScrollView: ScrollView
    };
})
