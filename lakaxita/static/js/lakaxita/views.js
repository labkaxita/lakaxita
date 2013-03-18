(function() {

    /*__________HELPERS__________*/

    Lakaxita.View = Backbone.View.extend({
        render: function() {
            this.$el.html(this.template(this));
            return this;
        },
    });

    Lakaxita.CollectionView = Backbone.View.extend({
        tagName: 'ul',
        render: function(event) {
            this.$el.empty();
            this.collection.each(function(model) {
                var view = new this.subView({model: model});
                this.$el.append(view.render().el);
            }, this);
            return this;
        },
    });


    /*__________INDEX__________*/

    Lakaxita.Index = Lakaxita.View.extend({
        template: Lakaxita.get_template('index'),
        initialize: function() {
            this.news = new Lakaxita.News();
            this.news.fetch();
            this.news.on('sync', this.render, this);
        },
    });


    /*__________LOST_FOUND__________*/

    Lakaxita.Item = Lakaxita.View.extend({
        tagName: 'li',
        template: Lakaxita.get_template('item'),
        title: function() { return this.model.title(); },
        hover: function() { return this.model.date(); },
        image: function() { return this.model.thumbnail(); },
        status: function() { return this.model.returned(); },
        url: function() { return this.model.absolute_url(); },
    });

    Lakaxita.ItemList = Lakaxita.CollectionView.extend({
        subView: Lakaxita.Item,
        initialize: function(options) {
            this.collection.on('sync', this.render, this);
        },
    });

    Lakaxita.ItemDetail = Lakaxita.Item.extend({
        tagName: 'article',
        template: Lakaxita.get_template('item-detail'),
        image: function() { return this.model.image(); },
    });

})()
