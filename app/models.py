from django.db import models

# Create your models here.
class Categories(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
      return self.name

class Tags(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
      return self.name

class Product(models.Model):
  def upload_image_to(self,filename):
    file='images'
    return f'{file}/{self.title}/{filename}'

  title = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  category= models.ForeignKey(Categories,on_delete=models.CASCADE)
  tags= models.ManyToManyField(Tags)
  trending = models.BooleanField(default=False)
  discount = models.BooleanField(default=False)
  mrp = models.IntegerField()
  discount_value = models.IntegerField(blank=True,null=True)
  final_price = models.IntegerField(blank=True,null=True)
  image1= models.ImageField(blank=False, upload_to=upload_image_to)
  image2= models.ImageField(blank=False, upload_to=upload_image_to)
  image3= models.ImageField(blank=False, upload_to=upload_image_to)
  image4= models.ImageField(blank=False, upload_to=upload_image_to)
  def __str__(self):
      return self.title

class Country(models.Model):
  name = models.CharField(max_length=200)
  prices = models.IntegerField()
  def __str__(self):
      return self.name

class Feedback(models.Model):
    stars=models.IntegerField(blank=True,null=False,default=1)
    feedback_note=models.TextField(null=True)
    img1=models.ImageField(blank=True,upload_to="img1/")
    img2=models.ImageField(blank=True,upload_to="img2/")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    #def __str__(self):
      #return product.title
class Blouse(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    price=models.IntegerField()
    description=models.TextField()
    def __str__(self):
      return self.title

class Order(models.Model):
    total=models.IntegerField()
    subtotal=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField(max_length=254)
    phone_number=models.BigIntegerField()
    order_note=models.CharField(max_length=150)
    shipping_charges=models.IntegerField()
    coupon_code=models.CharField(max_length=30)
    coupon_discount=models.IntegerField()
    order_receipt = models.CharField(max_length=50)
    order_id = models.CharField(max_length=20)
    razorpay_order_id = models.CharField(max_length=50)
    razorpay_payment_id = models.CharField(max_length=50)
    razorpay_signature = models.CharField(max_length=50)
    products = models.TextField()

    def __str__(self):
      return self.firstname

class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    mrp=models.IntegerField()
    discount_value=models.IntegerField()
    final_price=models.IntegerField()
    quantity=models.IntegerField()

class BlouseOrder(models.Model):
    order_item=models.ForeignKey(Blouse,on_delete=models.CASCADE,null=True)
    price=models.IntegerField()
