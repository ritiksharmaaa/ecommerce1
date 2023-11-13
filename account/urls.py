from django.urls import path 
from . views import (Registration_page  , Login_page  , Profile_page , address_page , address_update  , delete_address)
from .forms import  login_form , mypasswordResetForm , Password_ResetForm  , MySetPasswordForm 
# from django.contrib.auth.generic.views import auth_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("registration/"  , Registration_page.as_view() , name="registration"),
    
    path('login/' , auth_view.LoginView.as_view(template_name='acc/login.html' , authentication_form=login_form) , name='login'),
    path('logout/' , auth_view.LogoutView.as_view( template_name="acc/logout.html") , name='logout'),
    path('password-change/' , auth_view.PasswordChangeView.as_view( template_name="acc/passwordchange.html", form_class=mypasswordResetForm , success_url="/" ,  ) ,name='password-change'),
    path('password-reset/' , auth_view.PasswordResetView.as_view( template_name="acc/password_reset.html" , form_class=Password_ResetForm ) , name='password-reset'),
    path('password-reset/done/' , auth_view.PasswordResetDoneView.as_view(template_name="acc/password_reset_done.html" ) , name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/' , auth_view.PasswordResetConfirmView.as_view(template_name="acc/password_reset_confirm.html" , form_class=MySetPasswordForm ) , name='password_reset_confirm'),
    path('reset/done/' , auth_view.PasswordResetCompleteView.as_view(template_name="acc/password_reset_complete.html") , name="password_reset_complete" ),


    # profile related things 
    path('profile/', Profile_page.as_view(),  name="customer profile"),
    path('address/', address_page ,  name="customer address"),
    path('address/update/<int:id>/', address_update.as_view() ,  name="update-address"),
    path('address/deleted/<int:id>/', delete_address ,  name="delete-address"),
    
]
