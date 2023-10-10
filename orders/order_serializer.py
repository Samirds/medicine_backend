from rest_framework import serializers
from . models import Order_Details





class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Details
        fields = ["payment_transaction_id","ordered_at", "amount", "payment_transaction_id", "user_name", "user_email", "ordered_item_cat", "ordered_item_quantity", "is_paid", "cart","address", "phone", "delivery_status", "payment_type"]
        #fields = '__all__'




