define([
        'backbone', 
        'lakaxita/utils/loading', 
        'text',
        ], function(Backbone, Loading) {

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
        tagName: 'ul',
        className: 'scroll',
        initialize: function(options) {
            // make the el defined in the view child of 
            // the one that is passed alog
            var original_el = this.$el;
            options.el = null;
            this._configure(options);
            this._ensureElement();
            original_el.html(this.$el);

            this.collection.on('sync', this.render, this);
        },
        render: function() {
            Loading.show();
            this.$el.empty();
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                this.$el.append(view.render().el);
            }, this);
            Loading.hide();
            return this;
        },
        events: {
            'click li > a': 'remove',
        },
    });

    return {
        View: View,
        ScrollView: ScrollView
    };
})
