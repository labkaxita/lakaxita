define([
        'lakaxita/utils/views', 
        'lakaxita/groups/collections',
        ], function(Views, Collections) {

    Group = Views.View.extend({
        tagName: 'li',
        template: 'scroll_item',
        title: function() { return this.model.title(); },
        text: function() { return this.model.text(); },
        event: function() { return this.model.event(); },
        published: function() { return this.model.published(); },
        group: function() { return this.model.group(); },
        url: function() { 
            return this.router.getReverse('newsDetail', this.model);
        },
        icon: function() { return this.model.group()/*.image*/; },
        hover: function() { return this.model.published(); },
    });

    GroupScroll = Views.ScrollView.extend({
        className: 'news',
        subView: Group,
    });

    GroupDetail = News.extend({
        tagName: 'article',
        template: 'groups/group_detail',
        image: function() { return this.model.image(); },
    });

    return {
        GroupScroll: GroupScroll,
        GroupDetail: GroupDetail,
    };
})
