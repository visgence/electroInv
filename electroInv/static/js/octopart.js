$(function() {

    var spin_opts = {
        lines: 10, // The number of lines to draw
        length: 10, // The length of each line
        width: 5, // The line thickness
        radius: 5, // The radius of the inner circle
        corners: 1, // Corner roundness (0..1)
        rotate: 0, // The rotation offset
        direction: 1, // 1: clockwise, -1: counterclockwise
        color: '#000', // #rgb or #rrggbb or array of colors
        speed: 1, // Rounds per second
        trail: 60, // Afterglow percentage
        shadow: false, // Whether to render a shadow
        hwaccel: false, // Whether to use hardware acceleration
        className: 'spinner', // The CSS class to assign to the spinner
        zIndex: 2e9, // The z-index (defaults to 2000000000)
        top: 'auto', // Top position relative to parent in px
        left: 'auto' // Left position relative to parent in px
    };


    var updateParts = function() {
        var spinner = new Spinner(spin_opts).spin($('#spinner').get(0));
        
        var parts = [];
        $('.part-list li').each(function(i, li) {
            parts.push({'vendor': $(li).find('span').data('vendor'), 'sku': $(li).find('span').text()});
        });
        
        var data = {'parts': JSON.stringify(parts), 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()};
        $.post("/electroInv/octopart/update/", data, function(resp) {
            if(resp.hasOwnProperty('error')) { 
                $('#update-msg').html(resp['error']).addClass('text-danger'); 
                return;
            }

            $('#update-prompt').css('display', 'none');
            var errors = false;
            $.each(resp, function() {
                var span = $('span[data-vendor="'+this.vendor+'"][value="'+this.sku+'"]');
                if(this.error !== null) {
                    $(span).addClass('text-danger').append(this.error);
                    errors = true;
                }
                else
                    $(span).addClass('text-success');
            });

            if(errors)
                $('#update-msg').html("One or more parts did not successfully update.").addClass('text-danger');
            else
                $('#update-msg').html("All parts updated successfully!").addClass('text-success'); 
        }).
        fail(function(resp) {
            if(resp.hasOwnProperty('responseJSON'))
                $('#update-msg').html(resp['responseJSON']['error']).addClass('text-danger'); 
            else
                $('#update-msg').html("An unexpected error has occured.").addClass('text-danger'); 
        }).
        always(function() {
            spinner.stop();
        });
    };

    $.fn.updateParts = updateParts;
});
