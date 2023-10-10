from rest_framework import serializers
from . models import Payment_Detils





class pamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Detils
        fields = ["id", "amount", "payment_transaction_id", "user_name", "user_email", "ordered_item_cat", "ordered_item_quantity", "is_paid", "delivery_status", "cart"]
        #fields = '__all__'