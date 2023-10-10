from rest_framework import serializers
from .models import Product_Information



class Product_Info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Information
        fields = ['id', 'is_adv', 'availability', 'name', 'exp_date', 'price', 'Strip_contain', 'usage', 'is_corona_prod', "brand_type", 'brand', 'prod_age_cat', 'prod_type',  'image', 'prod_usage_cat', 'description', 'info']
        depth=1



from users.user_serializers import userSerialization

class combine(serializers.Serializer):
    pdi = Product_Information()
    use = userSerialization()

    class Meta:
        fields = ["pdi", "use"]