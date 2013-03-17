(function() {

    Lakaxita.CollectionView = Backbone.View.extend({
        tagName: 'ul',
        render: function() {
            this.$el.empty();
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                this.$el.append(view.render().el);
            }, this);
            return this;
        },
    });

    Lakaxita.Index = Backbone.View.extend({
        template: Lakaxita.get_template('index'),
        initialize: function() {
            this.news = new Lakaxita.News();
            this.news.on('all', this.render, this);
            this.news.fetch();
        },
        render: function() {
            this.$el.html(this.template(this));
            return this
        },
    });

    Lakaxita.Item = Backbone.View.extend({
        tagName: 'li',
        template: Lakaxita.get_template('item'),
        render: function() {
            this.$el.html(this.template(this));
            return this;
        },
        title: function() { return this.model.title(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.image(); },
        status: function() { return this.model.returned(); },
    });

    Lakaxita.ItemList = Lakaxita.CollectionView.extend({
        subView: Lakaxita.Item,
        initialize: function(options) {
            this.collection.on('all', this.render, this);
            this.collection.fetch();
        },
    });
})()
