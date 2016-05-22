$(document).ready(function(){
//
//focus on first input onload
//
    $(':input:enabled:visible:first').focus();    
//
//navigating through tabs
//
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });
    $('.nav-tabs a').on('shown.bs.tab', function(event){
        var x = $(event.target).text();         // active tab
        var y = $(event.relatedTarget).text();  // previous tab
        $(".act span").text(x);
        $(".prev span").text(y);
    });
});
    