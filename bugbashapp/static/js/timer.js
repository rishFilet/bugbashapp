var shortly = new Date();
shortly.setSeconds(shortly.getSeconds() + 5.5);
$(function() {
    $("#countdown").countdown({
        until: shortly,
  		onExpiry: liftOff //call this function and show the div
 	});
});

function liftOff(){
    $("#testing").show();
	shortly.setDate(shortly.getDate()+1);
	$("#countdown").countdown('option',{until:shortly})
}
