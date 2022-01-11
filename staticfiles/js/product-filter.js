$(document).ready(function () {
	if (performance.getEntriesByType('navigation')[0].type === 'back_forward') {
		location.reload();
	}
	// console.log('triggered');
	$('.select-all-filter').on('click', function () {
		// console.log('trigger');
		if ($(this).is(':checked')) {
			$('input:checkbox').prop('checked', true);
		} else {
			$('input:checkbox').prop('checked', false);
		}
	});

	$.ajax({
		url: '/on-page-load/',
		success: function (res) {
			if (res.value == 'All') $('input:checkbox').prop('checked', true);
			else {
				$('input[data-body=' + res.value + ']').prop('checked', true);
				filterOnLoad();
			}
			$.each(Object.keys(res.wishlist_obj), function (index, value) {
				// console.log(value);
				var val = document.querySelectorAll(
					`button#addToWishlist[data-id='${value}']`
				);
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

	function filterOnLoad() {
		$('.filter-checkbox').each(function () {
			var filterKey = $(this).data('filter');
			filterObj[filterKey] = Array.from(
				document.querySelectorAll(
					'input[data-filter=' + filterKey + ']:checked'
				)
			).map(function (el) {
				return el.value;
			});
		});
		ajaxFunc();
	}

	$("input[type='checkbox'].individual-category-main").change(function () {
		var a = $("input[type='checkbox'].individual-category-main");
		if (a.length == a.filter(':checked').length) {
			$('.select-all-filter').prop('checked', true);
			console.log('worked');
		} else {
			$('.select-all-filter').prop('checked', false);
		}
	});
	$("input[type='checkbox'].individual-category-modal").change(function () {
		var a = $("input[type='checkbox'].individual-category-modal");
		if (a.length == a.filter(':checked').length) {
			$('.select-all-filter').prop('checked', true);
			console.log('worked');
		} else {
			$('.select-all-filter').prop('checked', false);
		}
	});

	filterObj = {};
	$('.filter-checkbox').on('click', function () {
		$('.filter-checkbox').each(function () {
			var filterKey = $(this).data('filter');
			filterObj[filterKey] = Array.from(
				document.querySelectorAll(
					'input[data-filter=' + filterKey + ']:checked'
				)
			).map(function (el) {
				return el.value;
			});
		});
		ajaxFunc();
	});
	$(document).on('click', '.tag-btn', function () {
		if ($(this).hasClass('active')) $(this).removeClass('active');
		else $(this).addClass('active');
		$('.tag-btn').each(function () {
			var filterKey = $(this).data('tags');
			filterObj[filterKey] = Array.from(
				document.querySelectorAll('button.active')
			).map(function (el) {
				return el.value;
			});
		});
		ajaxFunc();
	});
	$(document).on('click', '.pagination-link', function () {
		filterObj['paginationval'] = $(this).text();
		ajaxFunc();
	});

	$(document).on('click', '.price-filter-btn', function () {
		filterObj['maxMinValues'] = Array.from([
			$('#slider').slider('values')[0],
			$('#slider').slider('values')[1],
		]);
		// console.log('Price filter ran');
		ajaxFunc();
	});

	$(document).on('change', '.price-ascending-descending', function () {
		if ($(this).find(':selected').val() == 'default') {
			filterObj['price-order'] = 0;
			// console.log(filterObj);
		}
		if ($(this).find(':selected').val() == 'low-high') {
			filterObj['price-order'] = 1;
			// console.log(filterObj);
		}
		if ($(this).find(':selected').val() == 'high-low') {
			filterObj['price-order'] = 2;
			// console.log(filterObj);
		}
		ajaxFunc();
	});

	function ajaxFunc() {
		$.ajax({
			url: '/filter-data/',
			data: filterObj,
			success: function (res) {
				$('#ajax-target-1').html(res.pagination_part1_obj);
				$('#ajax-target-2').html(res.product_list_obj);
				$('#ajax-target-3').html(res.pagination_part2_obj);
				ajaxFunc2();
			},
		});
	}

	function ajaxFunc2() {
		$.ajax({
			url: '/on-page-load/',
			success: function (res) {
				// console.log(Object.keys(res.wishlist_obj));
				$.each(Object.keys(res.wishlist_obj), function (index, value) {
					// console.log(value)
					var val = document.querySelectorAll(
						`button#addToWishlist[data-id='${value}']`
					);
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
	}
});

function setPaginationPageNum() {
	return false;
}
