//µ¼º½
$(window).scroll(ChangeNavbar);
function ChangeNavbar() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fcj").addClass("top-nav-collapse");
        $("#top").css("display","");
    } else {
        $(".navbar-fcj").removeClass("top-nav-collapse");
        $("#top").css("display", "none");
    }
    var scrollTop = $(document).scrollTop();
    var VivaTimelineHeight = $(".Demo1").offset().top;
    if ( scrollTop >= VivaTimelineHeight) {
        $(".pos-left").addClass("LeftInto");
        $(".pos-right").addClass("RightInto");
    }
    var ImageHeight = $(".Demo2").offset().top;
    if (scrollTop >= ImageHeight) {
        $(".box").addClass("RoateInto");
    }
    var GroupHeight = $(".Demo3").offset().top;
    if (scrollTop >= GroupHeight) {
        $("div[name='left']").addClass("LeftInto");
        $("div[name='right']").addClass("RightInto");
    }

}
$(function () {
    $('a.page-scroll').bind('click', function (event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutQuint');
        event.preventDefault();
    });

});
