"""kaliproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('collectionspage/', views.collectionspage, name="collectionspage"),
    path('collectionspage/<value>', views.collectionspage, name="collectionspage"),
    path('filter-data/',views.filterData,name='filterData'),
    path('ajax-cart-page/',views.ajaxCart,name='ajaxCart'),
    path('ajax-wishlist-page/',views.ajaxWishlist,name='ajaxCart'),
    path('on-page-load/',views.onPageLoad,name='onPageLoad'),
    path('add-to-cart/',views.addToCart,name='addToCart'),
    path('add-to-cart-extras/',views.addToCartExtras,name='addToCartExtras'),
    path('add-to-wishlist/',views.addToWishlist,name='addToWishlist'),
    path('delete-from-cart/',views.deleteFromCart,name='deleteFromCart'),
    path('delete-extras-from-cart/',views.deleteExtrasFromCart,name='deleteExtrasFromCart'),
    path('delete-from-wishlist/',views.deleteFromWishlist,name='deleteFromCart'),
    path('set-html/',views.setHtml,name='setHtml'),
    path('cart/',views.cart,name="cart"),
    # new additions below
    path('product/<int:id>/',views.product,name="product"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('billpage/',views.billpage,name="billpage"),
    path('country-shipping-charge/',views.shippingCharge,name="shippingCharge"),
    path('wishlist/',views.wishlistPage,name="wishlistPage"),
    path('select-design/',views.selectDesign,name='selectDesign'),
    path('confirm-billing-details/',views.confirmbilling,name="confirmbilling"),
    path('afterpayment/',views.afterpayment,name="afterpayment"),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
