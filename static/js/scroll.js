$(document).ready(function(){
    $("nav").find("a").click(function(e){
        e.preventDefault();
        var section = $(this).attr("href");
        $("html, body").animate({
            scrollTop: $(section).offset().top - 77
        }, 100, "linear");
    });
});
