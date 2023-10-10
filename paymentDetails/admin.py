from django.contrib import admin
from . models import Delivery_Status, Payment_Detils

# Register your models here.

@admin.register(Delivery_Status)
class Delivery_Status_Admin(admin.ModelAdmin):
    list_display = ["id", "status"]


@admin.register(Payment_Detils)
class payment_Detils_Admin(admin.ModelAdmin):
    list_display = ["id", "amount", "payment_transaction_id", "user_name", "user_email", "ordered_item_cat", "ordered_item_quantity", "is_paid", "delivery_status", "cart"]