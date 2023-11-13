from django.urls  import path 
from . import views 

urlpatterns = [
    path('' , views.Home , name="home"),
    path('category/<slug:val>/', views.CategoryView.as_view()  , name="catogory"),
    path('search/', views.search_product  , name="search"),
    path('cat/<str:val>/', views.categoryTitle.as_view()  , name="catogorytitle"),
    path('product/<int:pk>/', views.product_detail  , name="product-detail"),
    path('contact/' , views.contact_page , name="contact-page"),
    path('about/' , views.about_page , name="about-page"),



    # buying urls 
    path('add-to-cart/' , views.add_to_cart , name="addtocart"),
    path('plus-cart/' , views.plus_item , name="pluscart"),
    path('minus-cart/' , views.minus_item , name="minuscart"),
    path('removecart/' , views.remove_cart , name="removecart"),
    path('pluswishlist/' , views.plus_wishlist , name="plus wishlist"),
    path('minuswishlist/' , views.minus_wishlist , name="minus wishlist"),
    path('wishlist/' , views.wishlist_page , name="wishlist"),


    #orderplaced 
    path('cart/' , views.show_cart  , name="show cart"),
    path('checkout/' , views.checkout.as_view()  , name="checkout"),
    path('paymentdone/' , views.payment_done   , name="paymentdone"),
    path('paymentfailed/' , views.payment_failed   , name="paymentfailed"),
    path('order/' , views.order  , name="ordered_page"),
]
