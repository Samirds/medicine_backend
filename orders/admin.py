from django.contrib import admin
from .models import Order_Details, Delivery_Status, Payment_type
from django.utils.html import format_html

# Register your models here.

@admin.register(Delivery_Status)
class Delivery_Status_Admin(admin.ModelAdmin):
    list_display = ["id", "status"]




@admin.register(Payment_type)
class paymnt_type_Admin(admin.ModelAdmin):
    list_display = ["id", "type"]





@admin.register(Order_Details)
class Order_Detils_Admin(admin.ModelAdmin):
    list_display = ["payment_transaction_id","ordered_at", "amount",  "user_name", "user_email", "ordered_item_cat", "ordered_item_quantity", "is_paid", "cart","address", "phone", "delivery_status", "payment_type"]
    ordering = ["ordered_at"]



