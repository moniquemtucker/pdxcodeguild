/**
 * Created by monique tucker on 10/9/14.
 */
$(document).ready(function(){

    //slow scroll from main photo on home to start of carousel
    function scrollToCarousel(id){
        id = id.replace("link", "");
        $("html, body").animate({
            scrollTop: $("#" + id).offset().top
        }, 'slow')
    }

    $("#chevron").click(function(e) {
        e.preventDefault();
        scrollToCarousel("pp-carousel")
    });

    //fee structure is highlighted as cursor moves over it
    $(".fees-plans").hover(function(){
        $(this).toggleClass("active-fees-plans-head");
    });

});