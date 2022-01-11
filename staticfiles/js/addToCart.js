$(document).ready(function () {
	$(document).on('click', '#addToCart', function () {
		var id=$(this).attr('data-id');
    if ($(this).hasClass('active_btn')) {
      $(this).removeClass('active_btn');
      $.ajax({
        url:'/delete-from-cart/',
        data:{
          'id':id,
        },
        dataType:'json',
        success:function(res){
          console.log(res)
        }
      });
    }
		else 
    {
      $(this).addClass('active_btn');
      $.ajax({
        url:'/add-to-cart/',
        data:{
          'id':id,
          'quantity':1
        },
        dataType:'json',
        success:function(res){
          console.log(res)
        }
      });
    }
	});
});
