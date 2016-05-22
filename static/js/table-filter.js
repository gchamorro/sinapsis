$(document).ready(function () {

    (function ($) {

        $('#filter').keyup(function () {
//		input = $(this).val()
//		accentedInsensitive ='(<[^>]*>)|('+ search.replace(/[.+]i/,"$0") +')'
		var rex = new RegExp($(this).val(), 'ig');
            	$('.searchable tr').hide();
            	$('.searchable tr').filter(function () {
                return rex.test($(this).text());
            }).show();

        })

    }(jQuery));

    jQuery(document).ready(function($) {
        $(".clickable-row").click(function() {
            window.document.location = $(this).data("href");
        });
    });

});
