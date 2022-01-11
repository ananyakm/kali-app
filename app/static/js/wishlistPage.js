$(document).ready(function () {
  ajaxFunction()
  $(document).on('click', '.delete-from-wishlist', function () {
    var id=$(this).attr('data-id')
    deleteFromCart(id)
  })
  $(document).on('click', '.add-to-cart', function () {
    var id= $(this).attr('data-id')
    
    $.ajax({
      url:'/add-to-cart/',
      data:{
        'id':id,
        'quantity':1
      },
      dataType:'json',
      success:function(res){
        deleteFromCart(id)  
      }
    });
  })
})



function deleteFromCart(id){
  $.ajax({
    url:'/delete-from-wishlist/',
    data:{
      'id':id,
    },
    dataType:'json',
    success:function(res){
      ajaxFunction()
    }
  });
}

function ajaxFunction(){
  $.ajax({
    url: '/ajax-wishlist-page/',
    success: function (res) {
        $('#ajax-target-1').html(res.ajaxWishlistPage_obj);
    },
});
}