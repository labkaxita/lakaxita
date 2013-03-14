var NewsList = Backbone.Collection.extend({
    model: Backbone.Model.extend(),
    url: '/api/news/'
});
var News = new NewsList();


var GalleryList = Backbone.Collection.extend({
    model: Backbone.Model.extend(),
    url: '/api/gallery/'
});
var Gallery = new GalleryList();


var GroupList = Backbone.Collection.extend({
    model: Backbone.Model.extend(),
    url: '/api/groups/'
});
var Groups = new GroupList();


var ItemList = Backbone.Collection.extend({
    model: Backbone.Model.extend(),
    url: '/api/lost_found/'
});
var Items = new ItemList();


var AttachmentList = Backbone.Collection.extend({
    model: Backbone.Model.extend(),
    url: '/api/attachments/'
});
var Attachments = new AttachmentList();
