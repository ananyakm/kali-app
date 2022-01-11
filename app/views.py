from django.shortcuts import render,redirect
from django.http.response import Http404, JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Country, Product, Categories, Tags, Feedback, Blouse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.db.models import Sum
import razorpay
import random
import string
# Create your views here.


client = razorpay.Client(auth=("rzp_test_lYOMizShZ9dK1d", "FPZAwaMrz7DgYyvbPq1kOXSp"))
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def index(request):
  if request.method == 'GET':
    sarees= Product.objects.all().filter(trending=True)[:8]
    context={
      'saree_obj' : sarees
    }
    return render(request, 'index.html',context)

def collectionspage(request,value="All"):
  context={}
  page_num= request.GET.get('page')
  request.session['value']=value
  if request.method == 'GET':
    if value=='All':
      allProduct = Product.objects.all()
    elif value== 'Suits':
      allProduct = Product.objects.all().filter(category_id=1)
    elif value== 'Saree':
      allProduct= Product.objects.all().filter(category_id=2)
    else:
      raise Http404("Page does not exist")
    allProduct_paginator= Paginator(allProduct,16)
    allProduct_page= allProduct_paginator.get_page(page_num)
    context={
      'value':value,
      'tags_obj':Tags.objects.all(),
      'categories_obj':Categories.objects.all(),
      'saree_obj':allProduct_page,
      'paginator_val':allProduct_paginator,
      'page_obj':allProduct_page,
      'pages_range':allProduct_paginator.page_range,
      'start_index':allProduct_page.start_index(),
      'end_index':allProduct_page.end_index(),
    }
  return render(request,'collectionspage.html',context)


def filterData(request):
  category= request.GET.getlist('category[]')
  tags= request.GET.getlist('tags[]')
  paginationval=request.GET.getlist('paginationval')
  prices= request.GET.getlist('maxMinValues[]')
  if len(paginationval)>0:
    page_num=(paginationval[0])
  elif len(paginationval)==0:
    page_num=1
  price_order= request.GET.getlist('price-order')
  allProducts=Product.objects.all()
  check='all'
  if(any(check in category for category in category)):
    allProducts=allProducts
    if len(tags)>0:
      allProducts= allProducts.filter(tags__in=tags)
    if len(prices)>0:
      allProducts= allProducts.filter(mrp__range=(prices[0],prices[1]))
  else:
    if len(category)>0:
      allProducts= allProducts.filter(category_id__in=category)
    if len(tags)>0:
      allProducts= allProducts.filter(tags__in=tags)
    if len(prices)>0:
      allProducts= allProducts.filter(mrp__range=(prices[0],prices[1]))
    if len(price_order)>0:
      if(price_order[0]=='0'):
        allProducts=allProducts.order_by('id')
      elif(price_order[0]=='1'):
        allProducts=allProducts.order_by('mrp')
      elif(price_order[0]=='2'):
        allProducts=allProducts.order_by('-mrp')
  allProduct_paginator= Paginator(allProducts,16)
  allProduct_page= allProduct_paginator.get_page(page_num)
  context={
    'saree_obj':allProduct_page,
    'paginator_val':allProduct_paginator,
    'page_obj':allProduct_page,
    'pages_range':allProduct_paginator.page_range,
    'start_index':allProduct_page.start_index(),
    'end_index':allProduct_page.end_index(),
  }
  main_body=render_to_string('ajax/product-list.html',context)
  pagination_part1=render_to_string('ajax/pagination_part1.html',context)
  pagination_part2=render_to_string('ajax/pagination_part2.html',context)
  cart={}
  wishlist={}
  if 'wishlistdata' in request.session:
    wishlist=request.session['wishlistdata']
  if 'cartdata' in request.session:
    cart=request.session['cartdata']
  return JsonResponse({'product_list_obj':main_body,'pagination_part1_obj':pagination_part1,'pagination_part2_obj':pagination_part2, 'wishlist_obj': wishlist, 'cart_obj':cart})

def addToCart(request):
  cart={}
  cart[str(request.GET['id'])]=request.GET['quantity']
  if 'cartdata' in request.session:
      cart_data=request.session['cartdata']
      cart_data.update(cart)
      request.session['cartdata']=cart_data
  else:
    request.session['cartdata']=cart
  return JsonResponse({'cartdata':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

def addToCartExtras(request):
  cartExtra={}
  cartExtra[str(request.GET['id'])]=request.GET['quantity']
  if 'cartdataExtras' in request.session:
      cart_data=request.session['cartdataExtras']
      cart_data.update(cartExtra)
      request.session['cartdataExtras']=cart_data
  else:
    request.session['cartdataExtras']=cartExtra
  return JsonResponse({'cartdataExtras':request.session['cartdataExtras'],'totalitems':len(request.session['cartdataExtras'])})

def deleteFromCart(request):
  id=str(request.GET['id'])
  if 'cartdata' in request.session:
    if id in request.session['cartdata']:
      cart_data=request.session['cartdata']
      del request.session['cartdata'][id]
      request.session['cartdata']=cart_data
  return JsonResponse({'cartdata':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

def deleteExtrasFromCart(request):
  id=str(request.GET['id'])
  if 'cartdataExtras' in request.session:
    if id in request.session['cartdataExtras']:
      cart_data=request.session['cartdataExtras']
      del request.session['cartdataExtras'][id]
      request.session['cartdataExtras']=cart_data
  return JsonResponse({'cartdataExtras':request.session['cartdataExtras'],'totalitems':len(request.session['cartdataExtras'])})

def addToWishlist(request):
  wishlist={}
  wishlist[str(request.GET['id'])]={
    'id':request.GET['id'],
  }
  if 'wishlistdata' in request.session:
      wishlist_data=request.session['wishlistdata']
      wishlist_data.update(wishlist)
      request.session['wishlistdata']=wishlist_data
  else:
    request.session['wishlistdata']=wishlist
  # print(request.session['wishlistdata'])
  return JsonResponse({'wishlist':request.session['wishlistdata'],'totalitems':len(request.session['wishlistdata'])})

def deleteFromWishlist(request):
  id=str(request.GET['id'])
  if 'wishlistdata' in request.session:
    if id in request.session['wishlistdata']:
      wishlist_data=request.session['wishlistdata']
      del request.session['wishlistdata'][id]
      request.session['wishlistdata']=wishlist_data
  return JsonResponse({'wishlist':request.session['wishlistdata'],'totalitems':len(request.session['wishlistdata'])})


def onPageLoad(request):
  cart={}
  wishlist={}
  value={}
  if 'wishlistdata' in request.session:
    wishlist=request.session['wishlistdata']
  if 'cartdata' in request.session:
    cart=request.session['cartdata']
  if 'value' in request.session:
    value=request.session['value']
  return JsonResponse({'wishlist_obj':wishlist,'cart_obj':cart,'value':value})

def setHtml(request):
  val= request.GET['val']
  return JsonResponse({'val':val})

# new additions here
def product(request,id):
    if request.method=='GET':
        saree= Product.objects.get(id=id)
        rec_saree=Product.objects.all()

        related_products=Product.objects.filter(category=saree.category).exclude(id=id)
        for i in saree.tags.all():
          print(i.name)
          related_products=related_products.filter(tags__name=i.name)
          print(related_products)
        stars=[1,2,3,4,5]
        review=Feedback.objects.filter(product=saree)
        review_count=Feedback.objects.filter(product=saree).count()
        tags=Tags.objects.filter(product=saree)
        print(review_count)
        blouse=Blouse.objects.all()
    context={
        'saree' : saree,
        'rec_saree_obj':rec_saree,
        'review_obj':review,
        'related_obj':related_products,
        'blouse_obj':blouse,
        'stars':stars,
        'review_count':review_count,
        'tags':tags,

    }
    return render(request,'main-page.html',context)

def cart(request):


  if request.POST:
    Shoulder=request.POST.get('Shoulder')
    Shoulder_Full_Length=request.POST.get('Shoulder_Full_Length')
    Front_Neck_Depth=request.POST.get('Front_Neck_Depth')
    Chest=request.POST.get('Chest')
    Waist=request.POST.get('Waist')
    Back_neck_depth=request.POST.get('Back_neck_depth')
    Blouse_length=request.POST.get('Blouse_length')
    Sleeve_length=request.POST.get('Sleeve_length')
    Armhole=request.POST.get('Armhole')
    Sleeve=request.POST.get('Sleeve')
    size_details=[Shoulder,Shoulder_Full_Length,Front_Neck_Depth,Chest,Waist,Back_neck_depth,Sleeve_length,Armhole,Sleeve]
    print(size_details)
    request.session['designsize']=size_details
    return JsonResponse({'designsize':request.session['designsize'],'totalitems':len(request.session['designsize'])})


def cartpage(request):
  countries= Country.objects.all()
  context={
    'countries':countries
  }
  return render(request,'kali-cart.html',context)

def ajaxCart(request):
  cart={}
  cartExtras={}
  products=None
  blouse= None
  if 'cartdata' in request.session:
    cart=request.session['cartdata']
  dictval=list(cart.keys())
  quantities=list(cart.values())
  if 'cartdataExtras' in request.session:
    cartExtras=request.session['cartdataExtras']
  dictval2=list(cartExtras.keys())
  if len(dictval)>0:
    products= Product.objects.filter(id__in=dictval)
  if len(dictval2)>0:
    blouse= Blouse.objects.filter(id__in=dictval2)
    print(blouse)
  context={
    'dictval':dictval,
    'products':products,
    'quantities':quantities,
    'blouse':blouse,
  }
  if(products==None):
    ajaxCartPage= render_to_string('ajax/ajax-cart-empty.html')
    return JsonResponse({'ajaxCartPage_obj':ajaxCartPage,})
  else:
    ajaxCartPage= render_to_string('ajax/ajax-cart.html',context)
    ajaxCartPage_2= render_to_string('ajax/ajax-cart-2.html',context)

    return JsonResponse({'ajaxCartPage_obj':ajaxCartPage,'ajaxCartPage_2_obj':ajaxCartPage_2,})

def shippingCharge(request):
  countryname=request.GET['countryname']
  value=Country.objects.filter(name=countryname)
  l=[]
  l.append(countryname)
  l.append(value.first().prices)
  request.session['country'] = l
  print(l)
  context={
    'value':value
  }
  countryShippingCharges= render_to_string('ajax/ajax-cart-3.html',context)
  print("----------------------")
  return JsonResponse({'shippingCharges':countryShippingCharges})

def billpage(request):
    if request.method == "POST":
        request.session['firstname'] = request.POST['firstname']
        request.session['lastname'] = request.POST['lastname']
        request.session['countryname'] = request.POST['country']
        request.session['state'] = request.POST['state']
        request.session['addressline'] = request.POST['addressline']
        request.session['email'] = request.POST['email']
        request.session['phone'] = request.POST['phone']
        request.session['ordernotes'] = request.POST['ordernotes']
        return redirect("/confirm-billing-details/")
        pass
    country = request.session.get('country','None')
    cart = request.session['cartdata']
    productId_list = list(cart.keys())
    shipping_charge = country[1]

    l1=[]
    l2=[]
    subtotal = 0
    total = 0
    if len(productId_list)>0:
      products= Product.objects.filter(id__in=productId_list)
      for i in products:
          l=[]
          l.append(i)
          l.append(request.session['cartdata'][str(i.id)])
          l.append(i.final_price*int(request.session['cartdata'][str(i.id)]))
          subtotal = subtotal + (i.final_price*int(request.session['cartdata'][str(i.id)]))
          l1.append(l)
      print(l1)

    if 'cartdataExtras' in request.session:
      cartExtrasList=request.session['cartdataExtras']
      cartExtras= Blouse.objects.filter(id__in=cartExtrasList)
      for i in cartExtras:
          l=[]
          l.append(i)
          l.append(request.session['cartdataExtras'][str(i.id)])
          l.append(i.price*int(request.session['cartdataExtras'][str(i.id)]))
          subtotal = subtotal + (i.price*int(request.session['cartdataExtras'][str(i.id)]))
          l2.append(l)
      print(l2)
    total = shipping_charge + subtotal
    request.session['total_price'] = total
    context = {
        'country':country,
        'l1':l1,
        'l2':l2,
        'subtotal':subtotal,
        'total':total,
        'firstname':request.session.get('firstname',""),
        'lastname':request.session.get('lastname',""),
        'countryname':request.session.get('countryname',""),
        'state':request.session.get('state',""),
        'addressline':request.session.get('addressline',""),
        'email':request.session.get('email',""),
        'phone':request.session.get('phone',""),
        'ordernotes':request.session.get('ordernotes',""),

    }
    return render(request,'kali-billing.html',context)


def confirmbilling(request):
    country = request.session.get('country','None')
    cart = request.session['cartdata']
    productId_list = list(cart.keys())
    shipping_charge = country[1]

    l1=[]
    l2=[]
    subtotal = 0
    total = 0
    if len(productId_list)>0:
      products= Product.objects.filter(id__in=productId_list)
      for i in products:
          l=[]
          l.append(i)
          l.append(request.session['cartdata'][str(i.id)])
          l.append(i.final_price*int(request.session['cartdata'][str(i.id)]))
          subtotal = subtotal + (i.final_price*int(request.session['cartdata'][str(i.id)]))
          l1.append(l)
      print(l1)

    if 'cartdataExtras' in request.session:
      cartExtrasList=request.session['cartdataExtras']
      cartExtras= Blouse.objects.filter(id__in=cartExtrasList)
      for i in cartExtras:
          l=[]
          l.append(i)
          l.append(request.session['cartdataExtras'][str(i.id)])
          l.append(i.price*int(request.session['cartdataExtras'][str(i.id)]))
          subtotal = subtotal + (i.price*int(request.session['cartdataExtras'][str(i.id)]))
          l2.append(l)
      print(l2)
    total = shipping_charge + subtotal

    order_currency = 'INR'
    order_receipt = "KALI" + random_string_generator()
    request.session['order_receipt'] = order_receipt
    response = client.order.create(dict(amount=total*100, currency=order_currency, receipt=order_receipt, payment_capture='1'))
    order_id= response['id']
    request.session['order_id'] = order_id
    total_price = request.session.get('total_price')
    order_status = response['status']
    print(order_status)
    context = {
        'country':country,
        'l1':l1,
        'l2':l2,
        'subtotal':subtotal,
        'total':total,
        'firstname':request.session['firstname'],
        'lastname':request.session['lastname'],
        'countryname':request.session['countryname'],
        'state':request.session['state'],
        'addressline':request.session['addressline'],
        'email':request.session['email'],
        'phone':request.session['phone'],
        'ordernotes':request.session['ordernotes'],
    }
    if order_status == "created":
        context['order_id'] = order_id
        context['order_amount'] = total_price
        context['order_currency'] = order_currency
    else:
        return HttpResponse("Order not created")

    return render(request,'confirmbilling.html',context)




def wishlistPage(request):

  return render(request,'kali-wishlist.html')

def ajaxWishlist(request):
  wishlist={}
  products=None
  if 'wishlistdata' in request.session:
    wishlist=request.session['wishlistdata']
  dictval=list(wishlist.keys())
  if len(dictval)>0:
    products= Product.objects.filter(id__in=dictval)
  context={
    'products':products
  }
  if(products==None):
    ajaxWishlistPage= render_to_string('ajax/ajax-wishlist-empty.html')
  else:
    ajaxWishlistPage=render_to_string('ajax/ajax-wishlist.html',context)
  return JsonResponse({'ajaxWishlistPage_obj':ajaxWishlistPage})

def selectDesign(request):
  design={}
  id=request.GET.get('id')
  blouse=Blouse.objects.get(id=id)
  design.update({'id':blouse.id})

  design.update({'title':blouse.title})
  design.update({'image':blouse.image.url})

  design.update({'price':blouse.price})
  design.update({'description':blouse.description})
  print(design)
  if 'designdata' in request.session:
      design_data=request.session['designdata']
      design_data.update(design)
      request.session['designdata']=design_data
  else:
    request.session['designdata']=design
  return JsonResponse({'designdata':request.session['designdata'],'totalitems':len(request.session['designdata'])})
















def afterpayment(request):
  cart = request.session['cartdata']
  response = request.POST
  productId_list = list(cart.keys())
  params_dict = {
      'razorpay_payment_id' : response['razorpay_payment_id'],
      'razorpay_order_id' : response['razorpay_order_id'],
      'razorpay_signature' : response['razorpay_signature']
  }
  # VERIFYING SIGNATURE
  try:
    status = client.utility.verify_payment_signature(params_dict)
    product_list = []
    for i in productId_list:
      l = []
      p = Product.objects.get(pk=int(i))
      product = product + p.title + " Size-" + cart[i][0] + " Quantity-" + cart[i][1] + " /// "
      l.append(p.title)
      #l.append(your_cart[i][0])
      #l.append(your_cart[i][1])
      product_list.append(l)
    order = Product.objects.create(
            order_receipt= request.session['order_receipt'],
            order_id = request.session['order_id'],
            razorpay_payment_id = response['razorpay_payment_id'],
            razorpay_order_id = response['razorpay_order_id'],
            razorpay_signature = response['razorpay_signature'],
            name = request.session['first_name'] + " " + request.session['last_name'],
            address = request.session['street_address'] + "   " + request.session['street_address2'] + " City :- " + request.session['city'] + " State:- " + request.session['state'] + " Postcode:- "+ request.session['postcode'] ,
            phone_number = request.session['phone_number'],
            email = request.session['email'],
            final_price = request.session['total_price'],
            product = product,
        )
    #plaintext = get_template('emails/txtfiles/orderadmin.txt')
    #htmly= get_template('emails/orderadmin.html')
    #d = { 'order': order , 'product_list':product_list , 'total_price':request.session['total_price'] , 'subtotal_price':request.session['subtotal_price']  }
    #templateemail("Here's one order for you" , "jaiswalrina1985@gmail.com" , plaintext , htmly , d)
    #templateemail("We received your order" , request.session['email'] , plaintext , htmly , d)
    your_cart = ["your_cart"]
    request.session['cart'] = your_cart
    del request.session['first_name']
    del request.session['last_name']
    del request.session['street_address']
    del request.session['street_address2']
    del request.session['postcode']
    del request.session['city']
    del request.session['state']
    del request.session['phone_number']
    del request.session['email']
    del request.session['total_price']
    del request.session['order_receipt']
    del request.session['order_id']
    return HttpResponseRedirect('app:thankyou')
  except:
    return HttpResponse("Payment Failed")