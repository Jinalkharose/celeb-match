var image_file = null; 

function readURL(input) {
	if (input.files && input.files[0]) {

		var reader = new FileReader();
		image_file = input.files[0];

		reader.onload = function(e) {
			$('.image-upload-wrap').hide();
			$('.file-upload-image').attr('src', e.target.result);
			$('.file-upload-content').show();
			$('.image-title').html(input.files[0].name);
		};
		reader.readAsDataURL(input.files[0]);
	} else {
		removeUpload();
	}
}
	
function removeUpload() {
	var image_file = null;
	$('.file-upload-input').replaceWith($('.file-upload-input').clone());
	$('.file-upload-content').hide();
	$('.file-predicted-content').hide();
	$('.image-upload-wrap').show();
}

$('.image-upload-wrap').bind('dragover', function () {
	$('.image-upload-wrap').addClass('image-dropping');
});

$('.image-upload-wrap').bind('dragleave', function () {
	$('.image-upload-wrap').removeClass('image-dropping');
});

// Show the loader when an AJAX call starts
$(document).ajaxStart(function() {
	$('#loader').show();
});

// Hide the loader when an AJAX call is complete
$(document).ajaxStop(function() {
	$('#loader').hide();
});

function predict(){
	// Create a new FormData object
	var data = new FormData();
	var formData = $("#upload-form").serializeArray();
	
	$.each(formData, function(index, field) {
		data.append(field.name, field.value);
	});

	if (image_file){
		data.append('file', image_file);
	}

	// Send the data to the server using jQuery Ajax
	$.ajax({
		url: '/predict',
		type: 'POST',
		data: data,
		contentType: false,
		processData: false,
		success: function(response) {
			// Handle success response
			if (response.response == 'success') {
				$('#predicted_img').attr('src', response.file_path)
				$('#predicted_img_label').text(response.image_label)
				$('.file-predicted-content').show();
			}else{
				window.location.reload();
			}
		},
		error: function(xhr, status, error) {
			// Handle error response
			window.location.reload();
		}
	});
}
	