from django.shortcuts import render , HttpResponse , redirect
from django.db.models import Count 
from django.conf import settings 
# Create your views here.
from django.views import View 
from urllib import request 
from django.http import HttpResponse  ,HttpResponseRedirect  , JsonResponse 
from .models import Product , Cart , Customer_profile , Payment , OrderPlaced , wishlist 
from django.db.models import Q

from django.contrib.auth.decorators import login_required 

from django.utils.decorators import method_decorator 
import razorpay 

from django.contrib import messages



# creadtial of email or razorpay 
# your_script.py




def Home(request):
    totalitem = 0 
    totalwishlist = 0 
    if request.user.is_authenticated:
        totalwishlist = len(wishlist.objects.filter(user=request.user))

        totalitem = len(Cart.objects.filter(user=request.user))
    return render (request , 'app/index.html' , locals())
    # return HttpResponse(' i am running ')

#  show product with diffrent difrrent category . 

class  CategoryView(View):
    def get(self , request , val ):

        totalitem = 0 
        if request.user.is_authenticated:

            totalitem = len(Cart.objects.filter(user=request.user))
        obj = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        # title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        if len(obj) == 0 :
            obj = "sorry invalid category "
        else :
            obj = obj 
        # for obj in obj :
        #     print(obj.selling_price)
        return render(request , 'app/category.html' ,{'val' : val , 'pro' : obj , 'title' : title , 'totalitem':totalitem })



#  showing category title :  based product in single page 


class categoryTitle(View):
    def get(self , request , val):
        totalitem = 0 
        if request.user.is_authenticated:

            totalitem = len(Cart.objects.filter(user=request.user))
        print(val)
        obj = Product.objects.filter(title=val)

        title = Product.objects.filter(category=obj[0].category).values('title')
        
        # return HttpResponse(" i am working ")
        return render(request , 'app/category.html' , {'pro' : obj , 'title' : title , 'totalitem' : totalitem  })
    



#  showing product in detail page 

def product_detail(request  , pk ):
    totalitem = 0 
    obj =  Product.objects.get(id=pk)
    item_already_in_cart = False 
    wlist = False 
    wlist_len = 0
    if request.user.is_authenticated:
        wlist = wishlist.objects.filter(Q(Product=obj) & Q(user=request.user)).exists()
        totalitem = len(Cart.objects.filter(user=request.user))
        item_already_in_cart = Cart.objects.filter(Q(product=obj.id) & Q(user=request.user)).exists()
        wlist_len = len(wishlist.objects.filter(user=request.user))
    
    return render (request , 'app/productdetail.html' , {'data' : obj , "item_already_in_cart" : item_already_in_cart , 'totalitem' : totalitem  , 'wishlist' : wlist  , 'totalwishlist' : wlist_len})




# contect pge 
def contact_page(request):
    totalitem = 0 
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        print(totalitem)

    return render(request , 'app/contact.html' , locals())
# contect pge 
def about_page(request):
    totalitem = 0 
    if request.user.is_authenticated:

        totalitem = len(Cart.objects.filter(user=request.user))
        # print(totalitem + 100)
    return render(request , 'app/about.html' , locals())



@login_required
def add_to_cart(request):
    user = request.user
    product_id  = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    Cart(user=user , product=product).save()
    return HttpResponseRedirect("/cart")


@login_required
def plus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET.get("prod_id")
        product = Product.objects.get(id=prod_id)
        user = request.user 
        wishlist(user=user , Product=product).save()
        data = {
            'message ':  "item is add to wishlist"
        }
        return JsonResponse(data)



@login_required
def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET.get("prod_id")
        product = Product.objects.get(id=prod_id)
        user = request.user 
        wishlist.objects.filter(user=user , Product=product).delete()
        
        data = {
            'message ':  "item is remove from  wishlist"
        }
        return JsonResponse(data)
    return HttpResponse(status=404)
    

@login_required
def show_cart(request):
    totalitem = len(Cart.objects.filter(user=request.user)) # for notfication 
    user = request.user 
    data = Cart.objects.filter(user=user)
    amount= 0 
    for p in data:
        # print(p.product.discount_price)
        value = p.quantity *  p.product.discount_price 
        amount = amount + value 
    totalamount = amount + 40 
    # print(cart[0].product.title)
    print(totalamount)

    return render(request , "app/show_cart.html" , locals())


@login_required
def minus_item(request):
    if request.method == "GET":
        id = request.GET.get("prod_id")
        user = request.user
        cart_item = Cart.objects.get(Q(id=int(id)) & Q(user=user))
        
        cart_item.quantity =  cart_item.quantity - 1
        cart_item.save()
        

        cart = Cart.objects.filter(user=user)
        #cart item increase 
        amount= 0 
        totalamount=0
        for p in cart:
            # print(p.product.discount_price)
            value = p.quantity * p.product.discount_price 
            amount = amount + value 
            totalamount = amount + 40 
   
        data = {
            'amount' : amount ,
            'totalamount' : totalamount ,
            'quantity' : cart_item.quantity ,
            'msg' : "we deleted item succefulll as well return new amount and total amount"
        }
        return JsonResponse(data)

@login_required
def plus_item(request):
    if request.method == "GET":
        id = request.GET.get("prod_id")
        user = request.user
        cart_item = Cart.objects.get(Q(id=int(id)) & Q(user=user))
        cart_item.quantity = cart_item.quantity +  1
        cart_item.save()
        cart = Cart.objects.filter(user=user)
        #cart item increase 
        amount= 0 
        totalamount=0
        for p in cart:
            # print(p.product.discount_price)
            value = p.quantity * p.product.discount_price 
            amount = amount + value 
            totalamount = amount + 40 
   
        data = {
            'amount' : amount ,
            'totalamount' : totalamount ,
            'quantity' : cart_item.quantity ,
            'msg' : "we deleted item succefulll as well return new amount and total amount"
        }
        return JsonResponse(data)



@login_required
def remove_cart(request):
    if request.method == "GET":
        id = request.GET.get("prod_id")
        user = request.user 
        cart_item = Cart.objects.get(Q(id=int(id)) & Q(user=user)).delete()
        print(cart_item)
        print("data is deleted")
        data = Cart.objects.filter(user=user)
        amount= 0 
        totalamount=0
        for p in data:
            # print(p.product.discount_price)
            value = p.quantity * p.product.discount_price 
            amount = amount + value 
            totalamount = amount + 40 
   
        data = {
            'amount' : amount ,
            'totalamount' : totalamount ,
            'msg' : "we deleted item succefulll as well return new amount and total amount"
        }
        return JsonResponse(data)




class checkout(View):
    def get(self , request):
        user  = request.user
        add = Customer_profile.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount= 0 
        totalamount=0
        for p in cart_items:
            # print(p.product.discount_price)
            value = p.quantity * p.product.discount_price 
            amount = amount + value 
            totalamount = amount + 40 
        print(totalamount)
        razoramount = int(totalamount * 100)
        key_id = settings.RAZORPAY_KEY_ID
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID , settings.RAZORPAY_KEY_SECRET))
        client.set_app_details({"title" : "Django", "version" : "4.2.3"})
        data = {'amount' : razoramount , 'currency' : "INR" , "receipt" : "order_rcptid_11"}
        payment_response = client.order.create(data=data)
        # {'id': 'order_My2wfsZXj4hw5t', 'entity': 'order', 'amount': 539, 'amount_paid': 0, 'amount_due': 539, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1699461086}

        # print(payment_response)



        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == "created":
            payment = Payment(user=user , amount=totalamount , razorpay_order_id = order_id , razorpay_payment_status=order_status
            )
            payment.save()
   
        return render(request , "app/checkout.html" , locals())
    # def post(self , request):
    #     return render(request , "app/checkout.html" , locals())


@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get("cust_id")
    print(order_id , payment_id , cust_id)
    user = request.user 
    # return redirect order 
    customer = Customer_profile.objects.get(id=cust_id)
    # to update payment status
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True 
    payment.razorpay_payment_id = payment_id
    payment.save()
    cart = Cart.objects.filter(user=user)
    for cart_item in cart:
        OrderPlaced(user=user , customer=customer , product=cart_item.product, quantity=cart_item.quantity , payment=payment ).save()
        cart_item.delete()
    messages.success(request , "you order is succefully placed ! ")
    return HttpResponseRedirect("/order/")

@login_required
def payment_failed(request):
    # Extract error details from the query parameters
    error_code = request.GET.get('error_code')
    error_description = request.GET.get('error_description')
    error_source = request.GET.get('error_source')
    error_step = request.GET.get('error_step')
    error_reason = request.GET.get('error_reason')
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')


    return render(request , 'app/payment_failed.html' , locals())
        


                # code : response.error.code,
                # error_discription : response.error.description,
                # error_source : response.error.source,
                # erro_step : response.error.step ,
                # error_reason : response.error.reason ,
                # error_meta_data_order : response.error.metadata.order_id,
                # error_meta_data_payment : response.error.metadata.payment_id



@login_required
def order(request):

    totalitem = 0 
    if request.user.is_authenticated:

        totalitem = len(Cart.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request , "app/order.html" , locals())


@login_required
def wishlist_page(request):
    data = wishlist.objects.filter(user=request.user)
    return render(request , 'app/wishlist.html' , locals())


def search_product(request):
    query = request.GET.get('query')
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request , "app/search.html" , locals())