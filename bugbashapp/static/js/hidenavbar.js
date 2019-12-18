$(function() {
	$("a[href^='/register']").parent('li').css("display", "none");
	$("a[href^='/login']").parent('li').css("display", "none");
});
