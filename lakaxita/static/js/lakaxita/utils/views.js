define(['backbone'], function(Backbone) {

    View = Backbone.View.extend({
        render: function() {
            /* FIXME there must be a better way */
            var view = this
            require(['text!/template/'+this.template], function(template) {
                var template = Handlebars.compile(template);
                view.$el.html(template(view));
            });
            return this;
        },
    });

    ScrollView = Backbone.View.extend({
        tagName: 'ul',
        className: 'scroll',
        render: function(event) {
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
