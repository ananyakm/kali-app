$(document).ready(function () {
	if (performance.getEntriesByType('navigation')[0].type === 'back_forward') {
		location.reload();
	}
	// console.log('run')
	$.ajax({
		url: '/on-page-load/',
		success: function (res) {
			// console.log(res)
			$.each(Object.keys(res.wishlist_obj), function (index, value) {
				// console.log(value);
				var val = document.querySelectorAll(
					`button#addToWishlist[data-id='${value}']`
				);
				var val2= document.querySelectorAll(
					`div#addToWishlist[data-id='${value}']`
				);
				$(val2).addClass('active_btn');
				$(val).addClass('active_btn');
			});
			// console.log(Object.keys(res.cart_obj));
			$.each(Object.keys(res.cart_obj), function (index, value) {
				// console.log(value)
				var val = document.querySelectorAll(
					`button#addToCart[data-id='${value}']`
				);
				$(val).addClass('active_btn');
			});
		},
	});
});
