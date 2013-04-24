define([
        'backbone',
        'zen',
        'jquery.kinetic',
        'lakaxita/utils/views',
        'lakaxita/utils/app',
        'lakaxita/frontpage/collections',
        'lakaxita/news/app',
        ], function(
            Backbone,
            zen,
            $,
            Views,
            App,
            FrontpageCollections,
            NewsApp
            ) {


    SiteDescription = Views.View.extend({
        template: 'site_description',
    });

    Frontpage = Backbone.View.extend({
        initialize: function(options) {
            this.$el.empty();

            this.descriptionView = this.getDescriptionView();
            this.$el.append(this.descriptionView.el);

            this.newsView = this.getNewsView();
            this.$el.append(this.newsView.el);
            this.newsView.collection.fetch();

            // this.galleryView = this.getGalleryView();
            // this.$el.append(this.gallery.el);
        },
        getNewsView: function() {
            return NewsApp.FrontpageScroll({el: zen('section#news')});
        },
        getGalleryView: function() {
            return Gallery.Scroll({el: zen('section#gallery')});
        },
        getDescriptionView: function() {
            var collection = new FrontpageCollections.SiteDescription(),
                view = new SiteDescription({el: zen('section#description')});
            collection.on('sync', function() {
                var model = collection.at(0);
                view.model = model;
                view.render();
            });
            collection.fetch({prefill: true});
            return view;
        },
    });

    return {Frontpage: Frontpage};
})
