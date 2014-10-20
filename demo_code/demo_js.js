/**
 * Created by student on 10/9/14.
 */
//$(document).ready(function() {
//    $("#clickme").click(function () {
//        $("#go_away").slideToggle("slow", function () {
//// Animation complete.
//        });
//    });
//});

$(document).ready(function() {
   $('#go_away').mouseenter(function() {
       $(this).animate({
           height: '+=10px'
       });
   });
   $('#go_away').mouseleave(function() {
       $(this).animate({
           height: '-=10px'
       });
   });
   $('#go_away').click(function() {
       $(this).toggle(1000);
   });
});
