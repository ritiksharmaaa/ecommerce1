from django import forms 
from django.contrib.auth.forms import UserCreationForm  , AuthenticationForm , PasswordChangeForm , PasswordResetForm  , SetPasswordForm
from django.contrib.auth.models import User 
from app.models import Customer_profile  # we import from another application app 




class register_form(UserCreationForm):
    username = forms.CharField(label_suffix="" ,  error_messages={'required' : "username is required "}, widget=forms.TextInput(attrs={'autofocus' : 'True' , 'class' : 'form-control' }))
    email = forms.EmailField( label_suffix="" ,  error_messages={'required' : "Email is required "}, widget=forms.EmailInput(attrs={'class' : 'form-control ' }))
    password1 = forms.CharField( label="Password", label_suffix="" ,   error_messages={'required' : "Password  is required "} , widget=forms.PasswordInput(attrs={ 'class' : 'form-control  ' }))
    password2 = forms.CharField( label_suffix="" ,  error_messages={'required' : "again Password  is required "}, label="Confirm Password  " , widget=forms.PasswordInput(attrs={ 'class' : 'form-control ' }))

    field_order = ['username', 'email', 'password1', 'password2']

    class Meta :
        model = User 
        fields = ['username' , 'email' , 'password1' , 'password2']
    # use when we do something changes in other forms 



class login_form(AuthenticationForm):
    username =forms.CharField(label_suffix="" ,  error_messages={'required' : "username is required "}, widget=forms.TextInput(attrs={'autofocus' : 'True' , 'class' : 'form-control' }))
    password = forms.CharField( label="Password", label_suffix="" ,   error_messages={'required' : "Password  is required "} , widget=forms.PasswordInput(attrs={  'autocomplete' : 'current-password', 'class' : 'form-control  ' }))




class mypasswordResetForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'autofocus' : 'True' , 'autocomplete' : 'current-password' , 'class' : 'form-control'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={ 'autocomplete' : 'current-password' , 'class' : 'form-control'}))
    new_password2 = forms.CharField(label="Again  New  Password", widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password' , 'class' : 'form-control'}))

class Password_ResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={ 'autocomplete' : 'current-password' , 'class' : 'form-control'}))
    new_password2 = forms.CharField(label="Again  New  Password", widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password' , 'class' : 'form-control'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer_profile
        fields = [ 'name' ,'locality' , 'city' , 'mobile' ,'zipcode' , 'state']
        widgets={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'locality' : forms.TextInput(attrs={'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'state' : forms.Select(attrs={'class' : 'form-control'}),
            'zipcode' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }


# class UserProfile_form(UserProfile):
#     class Meta :
#         model = User 
#         fields = "__all__"