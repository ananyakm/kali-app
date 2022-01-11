from django.contrib import admin
from .models import Categories,Tags,Product,Country,Blouse, Feedback, Order, OrderItems,BlouseOrder
# Register your models here.

admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Blouse)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(BlouseOrder)