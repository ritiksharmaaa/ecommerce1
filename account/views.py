from django.shortcuts import render , redirect 
from django.http import HttpResponse  , HttpResponseRedirect 
from .forms import register_form  , login_form 
from django.views import View 
from django.contrib import messages
from .forms import CustomerProfileForm
from app.models import Customer_profile

from django.contrib.auth.decorators import login_required 

from django.utils.decorators import method_decorator 

# decorator = [never_cache , login_required , staff_login_required ] here order mathers 
# @method_decorator(decorator , name='dispatch')




# Create your views here.



class Registration_page(View):
    def get(self , request ):
        form = register_form()
        return render(request , 'acc/registration.html' , {'form' : form} )
    def post(self , request ):
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your are registerd  successful!")
            return HttpResponseRedirect("/accounts/registration/")
        else:
            messages.warning(request , "Invalid Input ")
        
        return render(request , 'acc/registration.html' , {'form' : form} )



class Login_page(View):
     def get(self , request ):
        form = login_form()
        return render(request , 'acc/login.html' , {'form' : form} )


@method_decorator(login_required , name="dispatch")
class Profile_page(View):
    def get(self , request):
        # data = Customer_profile.objects.filter(user=request.user)
        # print(data , '-------------------------------------------' , request.user)
        form = CustomerProfileForm()
        return render(request , 'acc/profile.html' , {'form' : form })
    def post(self , request , id=None):
        form = CustomerProfileForm(request.POST)
        # data = Customer_profile.objects.filter(user=request.user)
        if form.is_valid():
            # u_id = data[0].id
            user = request.user
            name = request.POST.get('name')
            locality = request.POST.get('locality')
            city  = request.POST.get('city')
            mobile  = request.POST.get('mobile')
            state  = request.POST.get('state')
            zipcode  = request.POST.get('zipcode')
            reg = Customer_profile( user=user , name=name , locality=locality , city=city , mobile=mobile , state=state , zipcode=zipcode ,)
            reg.save()
            messages.success(request , 'Congratulation ! Profile Saved Successfully')
        else:
            messages.warning(request , 'Invalid Data ! ')
        form = CustomerProfileForm()
        return render(request , 'acc/profile.html' , {'form' : form })

@login_required()
def address_page(request):
    data = Customer_profile.objects.filter(user=request.user)
    return render(request , 'acc/address.html' , {'add' : data })

@method_decorator(login_required , name="dispatch")
class address_update(View):
    def get(self , request , id=None ):
        instance = Customer_profile.objects.get(id=id)
        form = CustomerProfileForm(instance=instance)
        return render(request , "acc/address_update.html" , {'form' : form})
    def post(self , request  , id ):
        form = CustomerProfileForm( data=request.POST)
        if form.is_valid():
            add = Customer_profile.objects.get(id=id)
            add.name = request.POST.get('name')
            add.locality = request.POST.get('locality')
            add.city  = request.POST.get('city')
            add.mobile  = request.POST.get('mobile')
            add.state = request.POST.get('state')
            add.zipcode = request.POST.get('zipcode')
            add.save()
            messages.success(request , "Address Update Successfuly !  ")
        else:
            messages.warning(request , " Invalid Data ! ")
            return HttpResponseRedirect("/accounts/address/")
        # return HttpResponse("i am working ")

@login_required()
def delete_address( request , id ):
    data = Customer_profile.objects.get(id=id)
    data.delete()
    messages.success(request , "Address id deleted ")
    return HttpResponseRedirect("/accounts/address/")

