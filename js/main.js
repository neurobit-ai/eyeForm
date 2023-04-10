$(function() {

	'use strict';

	// Form

	var eyeForm = function() {

		if ($('#eyeForm').length > 0 ) {
			$( "#eyeForm" ).validate( {
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

					$('#caseNo').prop('disabled', false);
					$('#age').prop('disabled', false);
					$('#odRisk').val(localStorage.getItem('右眼'));
					$('#osRisk').val(localStorage.getItem('左眼'));
					$.ajax({   	
				      type: "POST",
				      url: "https://script.google.com/macros/s/AKfycbxqTvEUg2v4tQ2Y-mkFjAdt0R_DlnE3eG4y4Yc8GE6i9ZlpFz5xj2lwWx5mEsK9hBW46Q/exec",
				      data: $(form).serialize(),

				      beforeSend: function() { 
				      	$submit.css('display', 'block').text(waitText);
				      },
				      complete: function(msg) {
		               if (msg == '[object Object]') {
		               	$('#form-message-warning').hide();
				            setTimeout(function(){
		               		$('#eyeForm').fadeOut();
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
	eyeForm();

});
