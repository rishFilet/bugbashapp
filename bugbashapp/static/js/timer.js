$("#countdown").countdown({until: +400, format: 'MS', onExpiry: liftOff});
		function liftOff(){
			$(".popup-overlay, .popup-content").addClass("active");
			$(".submit-btn").css("visibility", "hidden");
		}
