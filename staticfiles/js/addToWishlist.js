$(document).ready(function () {
	$(document).on('click', '#addToWishlist', function () {
		var id=$(this).attr('data-id');
    if ($(this).hasClass('active_btn')) {
      $(this).removeClass('active_btn');
      $.ajax({
        url:'/delete-from-wishlist/',
        data:{
          'id':id,
        },
        dataType:'json',
        success:function(res){
          // console.log(res)
        }
      });
    }
		else 
    {
      $(this).addClass('active_btn');
      $.ajax({
        url:'/add-to-wishlist/',
        data:{
          'id':id,
        },
        dataType:'json',
        success:function(res){
          // console.log(res)
        }
      });
    }
    // console.log("test")

	});
});
