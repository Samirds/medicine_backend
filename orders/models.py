from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.

class Delivery_Status(models.Model):
     status = models.CharField(max_length=20, blank=True, null=True)
     def __str__(self):
         return self.status
     

class Payment_type(models.Model):
     type = models.CharField(max_length=20, blank=True, null=True)
     def __str__(self):
         return self.type


class Order_Details(models.Model):
    #order_id = models.CharField(max_length=50)
    payment_transaction_id = models.CharField(max_length=50, primary_key=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    ordered_item_cat=  models.CharField(max_length=50, default="Medicine")
    ordered_item_quantity = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    cart = models.JSONField(null=True)
    address = models.CharField(max_length=150)
    phone = PhoneNumberField()

    
    delivery_status = models.ForeignKey(Delivery_Status,on_delete=models.SET_NULL, null=True, verbose_name="Delivery Status")
    payment_type = models.ForeignKey(Payment_type,on_delete=models.CASCADE, null=True, verbose_name="Payment Type")





    def __str__(self):
         return self.ordered_item_cat