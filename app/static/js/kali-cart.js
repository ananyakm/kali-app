function add_item(){
    document.getElementById('quantity').innerHTML++;
}
// $(document).on('click', '#add-item', function () {
//     var val=$(this).attr('data-id2')
//     val1=document.querySelector(
//         "div[data-id='3']"
//     )
//     $.each(val1,function(){
//         console.log($(this).text())
//     })
// })
function remove_item(){
    if(document.getElementById('quantity').innerHTML>1)
    document.getElementById('quantity').innerHTML--;
}

$(document).ready(function () {

    ajaxCartPage()
    $(document).on('change', '.country-select', function () {
        countryname=$(this).find(':selected').val()
        $.ajax({
            url:'/country-shipping-charge/',
            data:{
                'countryname':countryname
            },
            success:function(res){
                $('#ajax-target-3').html(res.shippingCharges);
                findTotal()
            }
        })
   })
   $(document).on('click', '.delete-from-cart', function () {
       var id=$(this).attr('data-id')
       $.ajax({
        url:'/delete-from-cart/',
        data:{
          'id':id,
        },
        dataType:'json',
        success:function(res){
          ajaxCartPage()
        }
      });
   })
   $(document).on('click', '.delete-extra-from-cart', function () {
      var id=$(this).attr('data-id3')

       $.ajax({
        url:'/delete-extras-from-cart/',
        data:{
          'id':id,
        },
        dataType:'json',
        success:function(res){
          ajaxCartPage()
        }
      });
   })

})
var subtotal=0;
function ajaxCartPage(){
    $.ajax({
        url: '/ajax-cart-page/',
        success: function (res) {
            $('#ajax-target-1').html(res.ajaxCartPage_obj);

            if(res.ajaxCartPage_2_obj)
                $('#ajax-target-2').html(res.ajaxCartPage_2_obj);
            findSum()
        },
    });
}

function findSum(){
    val=document.querySelectorAll(
        '[data-value]'
      )
      subtotal=0
      $.each(val,function(){
        subtotal= subtotal + parseInt($(this).attr('data-value'))
      })
      $('#jquery-target-1').html("Rs."+subtotal.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
}
function findTotal(){
    shippingCharge = document.getElementById('shipping-charge').innerText
    total= parseInt(shippingCharge)+subtotal
    $('#jquery-target-2').html("Rs."+total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
}

function updateCart(){
    val=document.querySelectorAll(
        'div[data-id]'
      )
      $.each(val,function(){
        id=$(this).attr('data-id')
        quantity=$(this).text().replace(/\s+/g, ' ').trim()
        $.ajax({
            url:'/add-to-cart/',
            data:{
              'id':id,
              'quantity':quantity
            },
            dataType:'json',
            success:function(res){
              console.log(res)
            }
          });
      })
      val2=document.querySelectorAll(
        'div[data-id3]'
      )
      $.each(val2,function(){
        id=$(this).attr('data-id3')
        quantity=$(this).text().replace(/\s+/g, ' ').trim()
        $.ajax({
          url:'/add-to-cart-extras/',
          data:{
            'id':id,
            'quantity':quantity,
          },
          dataType:'json',
          success:function(res){
            console.log(res)
          }
        });
      })
}
