$("#countdown").countdown({until: +0, format: 'MS', onExpiry: liftOff});
		function liftOff(){
			$(".popup-overlay, .popup-content").addClass("active");
			$(".submit-btn").css("visibility", "hidden");
		}
