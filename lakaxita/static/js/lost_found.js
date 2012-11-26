notifications = {
    send: function() {
        $.ajax({
            url: $('form').attr('action'),
            type: 'POST',
            data: $('form').serialize(),
            success: function(data) {
                if (data.length == 0) {
                    $('section#notify form').hide();
                    $('section#notify p#successful').show();
                } else {
                    $('section#notify form').replaceWith(data);
                };
            }
        });
    },

    listen: function() {
        $('button#notify').click(function() {
            $('section#notify').show();
            $('form').live('submit', function(e) {
                e.preventDefault();
                notifications.send();
            });
        });
    }
};

$(function() {
    notifications.listen()
});
