$(document).ready(function () {
	$('a').click(function (event) {
		event.preventDefault();
		var page_n = $(this).attr('href');
		// ajax
		$.ajax({
			type: 'POST',
			url: "{% url 'pagination_p' %}", // name of url
			data: {
				page_n: page_n, //page_number
				csrfmiddlewaretoken: '{{ csrf_token }}',
			},
			success: function (resp) {
				//loop
				$('#posts').html('');
				$.each(resp.results, function (i, val) {
					//apending posts
					$('#posts').append('<h2>' + val.title + '</h2>');
				});
			},
			error: function () {},
		}); //
	});
});
