$("img.lazy").lazyload({
	effect : "fadeIn"
});
$("a.new-window, .footer-list a").click(function() {
	$(this).target = "_blank";
	location.replace(document.referrer);
	window.open($(this).prop("href"));
	// window.location.href = $(this).prop("href");
	return false
});
$("#notes a").click(function() {
	$(this).target = "_blank";
	window.open($(this).prop("href"));
	return false
});
$("a.email-lnk").each(function() {
	var e = $(this);
	var t = e.attr("href").split("||");
	e.attr("href", "mailto:" + t[1] + t[0])
});
var lastScrollTop = 0;
var distance = 200;
var nav = $(".nav-top");
var navHeight = $(".nav-top").outerHeight();
$(window).scroll(function() {
	var e = $(this).scrollTop();
	Math.abs(lastScrollTop - e) <= distance || (lastScrollTop > e ? ($("header.nav-top").addClass("nav-fixed"), setTimeout(function() {
		$("header.nav-top").removeClass("nav-fixed"), $(window).scrollTop() - 1e3 <= 0 ? $("header.nav-top").addClass("nav-fixed") : $("header.nav-top").removeClass("nav-fixed")
	}, 9e3)) : $("header.nav-top").removeClass("nav-fixed"), lastScrollTop = e);
	var t = $(window).scrollTop();
	if (t >= 5) {
		$("header").removeClass("nav-root")
	} else if (t <= 6) {
		$("header").addClass("nav-root")
	}
})