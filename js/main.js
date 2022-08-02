$(function() {

	'use strict';

	// Form

	var contactForm = function() {

		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					medRecNo: "required",
					site: "required",
					caseNo: "required",
					dateOfVisit: "required",
					dateOfBirth: "required",
					// name: "required",
					// email: {
					// 	required: true,
					// 	email: true
					// },
					// message: {
					// 	required: true,
					// 	minlength: 5
					// }
				},
				messages: {
					// name: "Please enter your name",
					// email: "Please enter a valid email address",
					// message: "Please enter a message"
				},
				/* submit via ajax */
				submitHandler: function(form) {		
					var $submit = $('.submitting'),
						waitText = '上 傳 中 . . .';

					$.ajax({   	
				      type: "POST",
				      url: "https://script.google.com/macros/s/AKfycbwr-fBTrxz1ZapFghTRcxedZQekgC5sRQajHBFYnry9tI7OLmnlK9dMgxvPMFTszLDGNg/exec",
				      data: $(form).serialize(),

				      beforeSend: function() { 
				      	$submit.css('display', 'block').text(waitText);
				      },
				      complete: function(msg) {
		               if (msg == '[object Object]') {
		               	$('#form-message-warning').hide();
				            setTimeout(function(){
		               		$('#contactForm').fadeOut();
		               	}, 100);
				            setTimeout(function(){
				               $('#form-message-success').fadeIn();   
		               	}, 1000);
			               
			            } else {
			               $('#form-message-warning').html(msg);
				            $('#form-message-warning').fadeIn();
				            $submit.css('display', 'none');
			            }
				      },
				      error: function() {
				      	$('#form-message-warning').html("Something went wrong. Please try again.");
				         $('#form-message-warning').fadeIn();
				         $submit.css('display', 'none');
				      }
			      });    		
		  		}
				
			} );
		}
	};
	contactForm();

});
