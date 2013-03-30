define(['backbone', 'text'], function(Backbone) {

    View = Backbone.View.extend({
        template_uri: function() {
            return 'text!/template/'+this.template+'/';
        },
        render: function() {
            var view = this;
            require([this.template_uri()], function(template) {
                var template = Handlebars.compile(template);
                view.$el.html(template(view));
            });
            return this;
        },
    });

    ScrollView = Backbone.View.extend({
        tagName: 'ul',
        className: 'scroll',
        initialize: function() {
            this.collection.on('sync', this.render, this);
        },
        render: function() {
            this.$el.empty();
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                this.$el.append(view.render().el);
            }, this);
            return this;
        },
    });

    return {
        View: View,
        ScrollView: ScrollView
    };
})
