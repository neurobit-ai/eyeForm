$(function() {

	'use strict';

	// Form

	var contactForm = function() {

		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					patientId: "required",
					dateOfVisit: "required",
					odDegree: "required",
					osDegree: "required",
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
						waitText = 'Submitting...';

					$.ajax({   	
				      type: "POST",
				      url: "https://script.google.com/macros/s/AKfycbz3OUsuq8INIJwUgUXuVQsPVqptM5sS65MoXV8q2HDvf4rNETfKrbf4lXbFJO5mJWQv/exec",
				      data: $(form).serialize(),

				      beforeSend: function() { 
				      	$submit.css('display', 'block').text(waitText);
				      },
				      success: function(msg) {
		               if (msg == 'OK') {
		               	$('#form-message-warning').hide();
				            setTimeout(function(){
		               		$('#contactForm').fadeOut();
		               	}, 1000);
				            setTimeout(function(){
				               $('#form-message-success').fadeIn();   
		               	}, 1400);
			               
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