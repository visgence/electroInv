$(function() {

    var updateParts = function() {
        var parts = [];
        $('.part-list li').each(function(i, li) {
            parts.push({'vendor': $(li).find('span').data('vendor'), 'sku': $(li).find('span').text()});
        });
        
        var data = {'parts': JSON.stringify(parts), 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()};
        $.post("/electroInv/octopart/update/", data, function(resp) {
            if(resp.hasOwnProperty('error')) { 
                $('#update-error').html(resp['error']); 
                return;
            }

            $('#update-prompt').css('display', 'none');
            $.each(resp, function() {
                var span = $('span[data-vendor="'+this.vendor+'"][value="'+this.sku+'"]');
                console.log(span);
                if(this.error !== null)
                    $(span).addClass('text-danger').append(this.error);
                else
                    $(span).addClass('text-success');
            });
        }).
        fail(function(resp) {
            if(resp.hasOwnProperty('responseJSON'))
                $('#update-error').html(resp['responseJSON']['error']); 
            else
                $('#update-error').html("An unexpected error has occured."); 
        });
    };

    $.fn.updateParts = updateParts;
});
