define([
        'backbone',
        'zen',
        'jquery.kinetic',
        'lakaxita/news/app',
        ], function(
            Backbone,
            zen,
            $,
            News
            ) {


    Frontpage = Backbone.View.extend({
        initialize: function(options) {
            this.news = zen('section#news');
            this.newsView = News.FrontpageScroll({el: this.news});

            this.$el.empty();
            this.news.kinetic({cursor: 'ew-resize'});
            this.$el.append(this.news);
            

            /* TODO: when gallery app ready
             * this.gallery = zen('section#gallery');
             * this.galleryView = Gallery.Scroll({el: this.gallery});
             * this.$el.append(this.gallery);
             * this.galleryView.collection.on(
             *                              'sync', 
             *                              this.galleryView.render, 
             *                              this.galleryView);
             */

            this.newsView.collection.on('sync', this.newsView.render, this.newsView);
        },
    });

    return {Frontpage: Frontpage};
})
