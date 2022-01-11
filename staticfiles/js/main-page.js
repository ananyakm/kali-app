function closeModal() {
	console.log('Cross button press');
	document.getElementById('modal').style.display = 'none';
}
function selectDesign(){
  document.getElementById('modal').style.display = 'none';
  document.getElementById('third-modal').style.display='none';
  document.getElementById('second-modal').style.display='flex';
}

function selectedDesign(){
  document.getElementById('second-modal').style.display='none';
  document.getElementById('second-modal-2').style.display='flex';

}
function closeSelectedDesign(){
  document.getElementById('second-modal-2').style.display="none";
}

function selectMeasurement(){
  document.getElementById('second-modal').style.display='none';

  document.getElementById('second-modal-2').style.display="none";
  document.getElementById('third-modal').style.display="flex";
}
function closeMeasurement(){
  document.getElementById('third-modal').style.display='none';
  document.getElementById('second-modal-2').style.display="none";}


function displayImg(value){
  document.getElementById('main-img').src=value;
}

function add_item(){
  document.getElementById('quantity').innerHTML++;
}
function remove_item(){
  if(document.getElementById('quantity').innerHTML >0)
  document.getElementById('quantity').innerHTML--;
}






     
    
$(document).ready(function () {
	$(document).on('click', '.blouseDesign', function () {
		var id=$(this).attr('data-id');
   
    $.ajax({
        url:'/select-design/',
        data:{
          'id':id,
        },
        dataType:'json',
        success:function(data){
          console.log(data)
          console.log(data['designdata']['id'])
          document.getElementById('modal-design-price').innerText=data['designdata']['price']
          document.getElementById('modal-design-title').innerText=data['designdata']['title']
          document.getElementById('modal-design-desc').innerText=data['designdata']['description']
          document.getElementById('modal-design-img').src=data['designdata']['image']
          ajaxCartExtra(data['designdata']['id'])
        }
      });
    
	
    console.log("test")
    document.getElementById('modal').style.display = 'none';
  document.getElementById('third-modal').style.display='none';
  document.getElementById('second-modal').style.display='flex';

	});
  
});

function ajaxCartExtra(id){
  $.ajax({
    url:'/add-to-cart-extras/',
    data:{
      'id':id,
      'quantity':1,
    },
    dataType:'json',
    success:function(res){
      console.log(res)
    }
  });
}

function closeDesign(){
  document.getElementById('second-modal').style.display='none';
}

/*
$(".rating a").on('click', function(e){
let value = $(this).data('value');
 $.ajax({
    url: "some_url",
    type: 'POST',
    data: {'rating': value},
    success: function (d){
     // some processing
    }
 })
});*/
$(document).ready(function () {
$(document).on('click','#addToCart',function(){

    var category=$(this).attr('data-category');

    
    document.getElementById('third-modal').style.display='none';
    if(category==2){
    	document.getElementById('modal').style.display = 'flex';
    }
});
});



