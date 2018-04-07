/*================================================================================
	Item Name: Materialize - Material Design Admin Template
	Version: 4.0
	Author: PIXINVENT
	Author URL: https://themeforest.net/user/pixinvent/portfolio
================================================================================

NOTE:
------
PLACE HERE YOUR OWN JS CODES AND IF NEEDED.
WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR CUSTOM SCRIPT IT'S BETTER LIKE THIS. */

function create_post() {
	$.ajax({
		url: url_home,
		type: "POST",
		data: {
			'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
			'name': $('#id_name').val(),
			'last_name': $('#id_last_name').val(),
			'occupation': $('#id_occupation').val(),
			'age': $('#id_age').val(),
		},
		success: function (json) {
			console.log(json)
		},
		error: function (xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
};

$(document).ready(function () {
		$('.modal').modal({
			dismissible: true, // Modal can be dismissed by clicking outside of the modal
			opacity: .5, // Opacity of modal background
			inDuration: 300, // Transition in duration
			outDuration: 200, // Transition out duration
			startingTop: '4%', // Starting top style attribute
			endingTop: '10%', // Ending top style attribute
			ready: function (modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
				console.log(modal, trigger);
			},
			complete: function () {} // Callback for Modal close
		});

		$('#cotizacion_btn').on('click', function (event) {
			console.log("submit");
			event.preventDefault();
			create_post();
		});
	}

);