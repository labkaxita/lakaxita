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

            this.setupDescription();
            this.setupNews();
            // this.setupGallery();

            this.$el.append(this.description);
            this.$el.append(this.news);
            this.$el.append(this.gallery);
        },
        setupNews: function() {
            this.news = zen('section#news');
            this.newsView = NewsApp.FrontpageScroll({el: this.news});
            this.newsView.collection.on('sync', this.newsView.render, this.newsView);
        },
        setupGallery: function() {
            this.gallery = zen('section#gallery');
            this.galleryView = Gallery.Scroll({el: this.gallery});
            this.galleryView.collection.on('sync', this.galleryView.render, 
                                         this.galleryView);
        },
        setupDescription: function() {
            var description = zen('section#description');
            this.description = description;
            var collection = new FrontpageCollections.SiteDescription();
            collection.on('sync', function() {
                var model = collection.at(0);
                this.descriptionView = new SiteDescription({model: model,
                    el: description});
                this.descriptionView.render();
            });
            collection.fetch({prefill: true});
        },
    });

    return {Frontpage: Frontpage};
})
