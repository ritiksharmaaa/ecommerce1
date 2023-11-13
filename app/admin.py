from django.contrib import admin
from . models import Product , Customer_profile  , Cart  , Payment , OrderPlaced , wishlist

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'selling_price' , 'category', 'product_img']




@admin.register(Customer_profile)
class Custom_profileAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name' , 'user' , 'locality' , 'city' , 'mobile' , 'zipcode' , 'state' ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'product' , 'quantity']



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user' , 'amount' , 'razorpay_order_id' , 'razorpay_payment_status' , 'razorpay_payment_id' , 'paid']
    

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display =['id' , 'user' , 'customer' , 'product' , 'quantity' , 'order_date' , 'status' , 'payment' ,'cost' ]


    
@admin.register(wishlist)
class wishlistAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'Product']
    
