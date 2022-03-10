$(function() {
    $('.form-group label').addClass('form-label fw-bolder text-dark fs-6');
    $('.form-group').addClass('fv-row mb-7 fv-plugins-icon-container');
    $('.form-group input').addClass('form-control form-control-lg form-control-solid');
    $('.form-group select').addClass('form-control form-control-lg form-control-solid');
    $('.form-group textarea').addClass('form-control form-control-lg form-control-solid');
});


function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		var cookies = document.cookie.split(";");
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

function removeCookie(name) {
	document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

const loader = '<div class="lds-dual-ring" id="ajxLoader"></div>'
function showLoader() {
	$('.content').css({ 'filter': 'blur(5px)' })
	$('.content-page').css({ 'filter': 'blur(5px)' })
	$('body').append(loader);
}
function removeLoader(status) {
	$('#ajxLoader').remove();
	if (status == false) {
		$('.content').css({ 'filter': 'none' })
		$('.content-page').css({ 'filter': 'none' })
	}

}


$(document).ready(function () {
	toast_message = getCookie('toast_message');
	toast_header = getCookie('toast_header');
	toast_type = getCookie('toast_type');
	if (toast_message !== null) {
		try {
			toast_message = JSON.parse(toast_message);
			toast_header = JSON.parse(toast_header);
		} catch (error) {
			toast_message = toast_message;
			toast_header = toast_header;
		}
		toastr.options = {
			"closeButton": false,
			"debug": false,
			"newestOnTop": false,
			"progressBar": false,
			"positionClass": "toast-top-right",
			"preventDuplicates": false,
			"onclick": null,
			"showDuration": "300",
			"hideDuration": "1000",
			"timeOut": "5000",
			"extendedTimeOut": "1000",
			"showEasing": "swing",
			"hideEasing": "linear",
			"showMethod": "fadeIn",
			"hideMethod": "fadeOut"
		};

		switch (toast_type) {
			case "success":
				toastr.success(toast_message, toast_header);
				break;
			case "info":
				toastr.info(toast_message, toast_header);
				break;
			case "warning":
				toastr.warning(toast_message, toast_header);
				break;
			case "error":
				toastr.error(toast_message, toast_header);
				break;
			default:
				toastr.error(toast_message, toast_header);
				console.error("\nUnexpected type for toast_message in django views\n")
		}
		removeCookie('toast_message')
		removeCookie('toast_type');
		removeCookie('toast_header');
	}

	$(document).on('submit', 'form.ajax', function (e) {
		e.preventDefault();
		$('.response-message-box').addClass('d-none');
		$('.response-message').empty();
		var $this = $(this);
		var url = $this.attr('action');
		var method = $this.attr('method');
		var isReset = $this.hasClass('reset');
		var isReload = $this.hasClass('reload');
		var isRedirect = $this.hasClass('redirect');
		var isSwal = $this.hasClass('swal');
		var isAlert = $this.hasClass('showalert');
		showLoader();
		jQuery.ajax({
			type: method,
			url: url,
			dataType: 'json',
			data: new FormData(this),
			contentType: false,
			cache: false,
			processData: false,
			success: function (data) {
				removeLoader(true);
				var message = data['message'];
				var status = data['status'];
				var title = data['title'];
				var redirect = data['redirect'];
				var redirect_url = data['redirect_url'];
				var stable = data['stable'];
				if (stable === null || stable === undefined) {
					stable = "false";
				}
				if (status == 'true') {
					if (title) {
						title = title;
					} else {
						title = "Success";
					}
					function redirectPage() {
						if (stable != "true") {
							if (isRedirect && redirect == 'true') {
								window.location.href = redirect_url;
							}
							if (isReload) {
								window.location.reload();
							}
						}
					}
					Swal.fire({
						icon: 'success',
						title: title,
						text: message,
					}).then((response) => {
						redirectPage();
					})
				}
				else {
					removeLoader(false);
					if (title) {
						title = title;
					}
					else {
						title = "Something went wrong";
					}
					if (isSwal) {
						Swal.fire(title, message, 'error')
						if (stable != "true") {
							window.setTimeout(function () {
							}, 2000);
						}
					}
					else if (isAlert) {
						var alertmessage = message.replace('|', ' ')
						$('.response-message-box').removeClass('d-none');
						$('.response-message').text(alertmessage);
						window.scrollTo(0, 0);
						redirectPage();
					}
					else {
						Swal.fire(title, message, 'error')
						if (stable != "true") {
							window.setTimeout(function () {
							}, 2000);
						}
					}
				}

			},
			error: function (data) {
				removeLoader(false);
				var title = "An error occurred";
				var message = "Please try again later.";
				document.onkeydown = function (evt) {
					return true;
				};
				Swal.fire(title, message, 'error')
			}
		});
	});


	$(".tt-del-btn").click(function (e) {
		e.preventDefault();
		var $this = $(this);
		var url = $this.attr('href');
		var revoke = $this.hasClass('revoke-btn');
		let timerInterval
		const swalWithBootstrapButtons = Swal.mixin({
			customClass: {
				confirmButton: 'btn btn-danger',
				cancelButton: 'btn btn-success'
			},
			buttonsStyling: false
		})
		function deleteAjax(url) {
			showLoader();
			jQuery.ajax({
				type: "POST",
				url: url,
				dataType: 'json',
				headers: { "X-CSRFToken": getCookie("csrftoken") },
				success: function (data) {
					removeLoader(true);
					var message = data['message']
					var status = data['status']
					var redirect_url = data['redirect_url'];

					var title = "Deleted"
					if (revoke) {
						title = "Revoked"
					}
					if (status == 'false') {
						title = "Error"
						Swal.fire(title, message, 'error')
						removeLoader(false);
					}
					else {
						Swal.fire({
							icon: 'success',
							title: title,
							text: message,
						}).then(() => {
							window.location.href = redirect_url;
						})
					}
				},
				error: function (data) {
					removeLoader(false);
					var title = "An error occurred";
					var message = "Please try again later.";
					document.onkeydown = function (evt) {
						return true;
					};
					Swal.fire(title, message, 'error')
				}
			});
		}
		if (revoke) {
			var confirmText = 'Yes, revoke user'
			var postCancel = 'User still active'
		} else {
			var confirmText = 'Yes, delete'
			var postCancel = 'Your data is safe'
		}

		swalWithBootstrapButtons.fire({
			title: 'Are you sure?',
			text: "You won't be able to revert this!",
			icon: 'warning',
			showCancelButton: true,
			confirmButtonText: confirmText,
			cancelButtonText: "No, cancel",
			reverseButtons: true
		}).then((result) => {
			if (result.value) {
				showLoader();
				if (revoke) {
					Swal.fire({
						title: 'Warning!',
						icon: 'warning',
						html: "Revoking in <b></b> seconds",
						timer: 1500,
						confirmButtonText: "No, cancel",
						timerProgressBar: true,
						willOpen: () => {
							//   Swal.showLoading()
							timerInterval = setInterval(() => {
								const content = Swal.getContent()
								if (content) {
									const b = content.querySelector('b')
									if (b) {
										time = Swal.getTimerLeft()
										b.textContent = Math.round(time / 1000)
									}
								}
							}, 100)
						},
						onClose: () => {
							removeLoader(false);
							clearInterval(timerInterval)
						}
					}).then((result) => {
						if (result.dismiss === Swal.DismissReason.timer) {
							deleteAjax(url);
						}
					})
				} else {
					deleteAjax(url);
				}
			} else if (
				result.dismiss === Swal.DismissReason.cancel
			) {
				Swal.fire(
					'Cancelled',
					postCancel,
					'error'
				)
			}
		})
	});

	// UPDATE
	$(".tt-update-btn").click(function (e) {
		e.preventDefault();
		var $this = $(this);
		var url = $this.attr('href');
		var revoke = $this.hasClass('revoke-btn');
		let timerInterval
		const swalWithBootstrapButtons = Swal.mixin({
			customClass: {
				cancelButton: 'btn btn-danger',
				confirmButton: 'btn btn-success'
			},
			buttonsStyling: false
		})
		function deleteAjax(url) {
			showLoader();
			jQuery.ajax({
				type: "POST",
				url: url,
				dataType: 'json',
				headers: { "X-CSRFToken": getCookie("csrftoken") },
				success: function (data) {
					removeLoader(true);
					var message = data['message']
					var status = data['status']
					var redirect_url = data['redirect_url'];

					var title = "Completed"
					if (revoke) {
						title = "Revoked"
					}
					if (status == 'false') {
						title = "Error"
						Swal.fire(title, message, 'error')
						removeLoader(false);
					}
					else {
						Swal.fire({
							icon: 'success',
							title: title,
							text: message,
						}).then(() => {
							window.location.href = redirect_url;
						})
					}
				},
				error: function (data) {
					removeLoader(false);
					var title = "An error occurred";
					var message = "Please try again later.";
					document.onkeydown = function (evt) {
						return true;
					};
					Swal.fire(title, message, 'error')
				}
			});
		}
		if (revoke) {
			var confirmText = 'Yes, revoke user'
			var postCancel = 'User still active'
		} else {
			var confirmText = 'Yes, Completed'
			var postCancel = 'Complete Tour Tasks!'
		}

		swalWithBootstrapButtons.fire({
			title: 'Are you sure?',
			text: "You won't be able to revert this!",
			icon: 'warning',
			showCancelButton: true,
			confirmButtonText: confirmText,
			cancelButtonText: "No, cancel",
			reverseButtons: true
		}).then((result) => {
			if (result.value) {
				showLoader();
				if (revoke) {
					Swal.fire({
						title: 'Warning!',
						icon: 'warning',
						html: "Revoking in <b></b> seconds",
						timer: 1500,
						confirmButtonText: "No, cancel",
						timerProgressBar: true,
						willOpen: () => {
							//   Swal.showLoading()
							timerInterval = setInterval(() => {
								const content = Swal.getContent()
								if (content) {
									const b = content.querySelector('b')
									if (b) {
										time = Swal.getTimerLeft()
										b.textContent = Math.round(time / 1000)
									}
								}
							}, 100)
						},
						onClose: () => {
							removeLoader(false);
							clearInterval(timerInterval)
						}
					}).then((result) => {
						if (result.dismiss === Swal.DismissReason.timer) {
							deleteAjax(url);
						}
					})
				} else {
					deleteAjax(url);
				}
			} else if (
				result.dismiss === Swal.DismissReason.cancel
			) {
				Swal.fire(
					'Cancelled',
					postCancel,
					'error'
				)
			}
		})
	});





	$(document).on('submit', 'form.celery-uploader', function (e) {
		e.preventDefault();

		$(':input[type="submit"]').prop('disabled', true);
		$('.console').removeClass('d-none');
		$('.transcoding').parent().removeClass('d-none');

		var $this = $(this);
		var url = $this.attr('action');
		var method = $this.attr('method');
		var isReset = $this.hasClass('reset');
		var isReload = $this.hasClass('reload');
		var isRedirect = $this.hasClass('redirect');
		$('.progress').removeClass("d-none");
		jQuery.ajax({
			xhr: function () {
				var xhr = new window.XMLHttpRequest();
				xhr.upload.addEventListener('progress', function (e) {
					if (e.lengthComputable) {
						var percent = Math.round((e.loaded / e.total) * 100);
						$('.progress-bar.uploading').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
					}
				});
				return xhr;
			},
			type: method,
			url: url,
			dataType: 'json',
			data: new FormData(this),
			contentType: false,
			cache: false,
			processData: false,
			success: function (data) {
				var message = data['message'];
				var status = data['status'];
				var title = data['title'];
				var redirect = data['redirect'];
				var redirect_url = data['redirect_url'];
				var stable = data['stable'];

				var task_id = data['task_id'];
				$('input[name="task"]').val(task_id);

				if (stable === null || stable === undefined) {
					stable = "false";
				}

				if ($('.progress-bar.uploading').attr('aria-valuenow') == "100") {
					$('.post-upload').text("Uploading Completed")
					setTimeout(function () {
						$('.transcoding').text("Fetching Files...")
					}, 2000);

					var current_status, state, progressUrl = `course/${task_id}`;

					function updateProgress(progressUrl) {
						fetch(progressUrl).then(function (response) {
							response.json().then(function (data) {
								state = data.state;
								if (state == "PENDING") {
									state = "PROCESSING";
								}
								$('.transcoding').text(state);
								setTimeout(updateProgress, 10000, progressUrl);
								current_status = $('.transcoding').text();
								if (current_status == "SUCCESS") {
									clearTimeout();
									setTimeout(function () {
										postTranscoding();
									}, 2000);
								}
							});
						});
					}
					updateProgress(progressUrl);

					function postTranscoding() {
						if (status == 'true') {
							if (title) {
								title = title;
							} else {
								title = "Success";
							}

							function redirectPage() {
								if (stable != "true") {
									if (isRedirect && redirect == 'true') {
										window.location.href = redirect_url;
									}
									if (isReload) {
										window.location.reload();
									}
								}
							}

							Swal.fire({
								icon: 'success',
								title: title,
								text: message,
							}).then((response) => {
								redirectPage();
							})
						}
						else {
							if (title) {
								title = title;
							}
							else {
								title = "Something went wrong";
							}
							Swal.fire(title, message, 'error')
							if (stable != "true") {
								window.setTimeout(function () {
								}, 2000);
							}
						}
					}

				}

			},
			error: function (data) {
				var title = "An error occurred";
				var message = "Please try again later.";
				document.onkeydown = function (evt) {
					return true;
				};
				Swal.fire(title, message, 'error')
			}
		});
	});



	$(document).on('submit', 'form.video-uploader', function (e) {
		e.preventDefault();
		// $(':input[type="submit"]').prop('disabled', true);

		var isVideo = true;
		var element = $("#id_video").val();
		if (element == "" || element == null) {
			isVideo = false;
		}
		var $this = $(this);
		var url = $this.attr('action');
		var method = $this.attr('method');
		var isReset = $this.hasClass('reset');
		var isReload = $this.hasClass('reload');
		var isRedirect = $this.hasClass('redirect');

		if (isVideo == true) {
			$('.progress').removeClass("d-none");
		}
		jQuery.ajax({
			xhr: function () {
				var xhr = new window.XMLHttpRequest();
				xhr.upload.addEventListener('progress', function (e) {
					if (e.lengthComputable) {
						var percent = Math.round((e.loaded / e.total) * 100);
						$('.progress-bar.uploading').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
					}
				});
				return xhr;
			},
			type: method,
			url: url,
			dataType: 'json',
			data: new FormData(this),
			contentType: false,
			cache: false,
			processData: false,
			success: function (data) {
				var message = data['message'];
				var status = data['status'];
				var title = data['title'];
				var redirect = data['redirect'];
				var redirect_url = data['redirect_url'];
				var stable = data['stable'];
				if (stable === null || stable === undefined) {
					stable = "false";
				}


				if ($('.progress-bar.uploading').attr('aria-valuenow') == "100") {
					$('.post-upload').text("Uploading Completed")
					setTimeout(function () {
					}, 3000);

					if (status == 'true') {
						if (title) {
							title = title;
						} else {
							title = "Success";
						}

						function redirectPage() {
							if (stable != "true") {
								if (isRedirect && redirect == 'true') {
									window.location.href = redirect_url;
								}
								if (isReload) {
									window.location.reload();
								}
							}
						}

						Swal.fire({
							icon: 'success',
							title: title,
							text: message,
						}).then((response) => {
							redirectPage();
						})
					}
					else {
						if (title) {
							title = title;
						}
						else {
							title = "Something went wrong";
						}
						Swal.fire(title, message, 'error')
						if (stable != "true") {
							window.setTimeout(function () {
							}, 2000);
						}
					}


				}

			},
			error: function (data) {
				var title = "An error occurred";
				var message = "Please try again later.";
				document.onkeydown = function (evt) {
					return true;
				};
				Swal.fire(title, message, 'error')
			}
		});
	});

});
