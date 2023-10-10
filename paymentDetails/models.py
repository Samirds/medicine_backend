from django.db import models

# Create your models here.

class Delivery_Status(models.Model):
     status = models.CharField(max_length=20, blank=True, null=True)
     def __str__(self):
         return self.status

class Payment_Detils(models.Model):
    #order_id = models.CharField(max_length=50)
    amount = models.PositiveIntegerField(default=0)
    payment_transaction_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    ordered_item_cat=  models.CharField(max_length=50, default="Medicine")
    ordered_item_quantity = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    cart = models.JSONField(null=True)
    

    
    delivery_status = models.ForeignKey(Delivery_Status,on_delete=models.SET_NULL, null=True, verbose_name="Delivery Status")




    def __str__(self):
         return self.ordered_item_cat