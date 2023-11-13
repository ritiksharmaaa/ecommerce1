from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = [
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Uttar pradesh', 'Uttar pradesh '),

]








CATEGORY_CHOICES = [
    ('CR' , 'Curd'),
    ('ML' , 'Milk'),
    ('LS' , 'lassi'),
    ('MS' , 'MilkShake'),
    ('PN' , 'Panner'),
    ('GH' , 'Ghee'),
    ('CH' , 'Cheese'),
    ('Ic' , 'Ice-Creame'),
]



STATUS_CHOICES = [
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('on The Way ' ,'on The Way ed'),
    ('Delivered' , 'Delivered'),
    ('Cancel' , 'Cancel'),
    ('Pending' ,'Pending'),
]
class Product(models.Model):
    title = models.CharField( max_length=50)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    discription = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=2)
    product_img = models.ImageField( upload_to="Product")

    def __str__(self):
        return self.title


class Customer_profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField( max_length=250)
    locality = models.CharField( max_length=200)
    city = models.CharField( max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,  max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product ,  on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default="1")

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price 






# order placed : we need one payment tabel and one order table . 

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField( max_length=100 , blank=True , null=True)
    razorpay_payment_status = models.CharField( max_length=100 , blank=True , null=True)
    razorpay_payment_id = models.CharField( max_length=100 , blank=True , null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE )
    customer = models.ForeignKey(Customer_profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField( auto_now_add=True)
    status = models.CharField( max_length=50,   choices=STATUS_CHOICES , default="Pending")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE , default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

    def cost(self):
        return self.quantity * self.product.discount_price



class wishlist(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    