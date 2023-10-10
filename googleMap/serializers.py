# from rest_framework import serializers
# from django.core.exceptions import ValidationError
# from .models import SaveUserAddress


# class userSerializers(serializers.Serializer):   # here we are not using model serializers because we don't want to craeate any mdoel
#     lat = serializers.DecimalField(max_digits=19, decimal_places=15,)
#     lang = serializers.DecimalField(max_digits=19, decimal_places=15,) 

#     def validate(self, data):
#         lat = data.get("lat")
#         lang = data.get("lang")

#         if not lat:
#             raise ValidationError("latitude is required")
#         if not lang:
#             raise ValidationError("Longitude is required")
#         # if lat <0:
#         #     raise ValidationError("latitude can' be less than zero")
#         # if lang <0:
#         #     raise ValidationError("Longitude can' be less than zero")
        
#         return data
    

# class saveUserAddressSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model = SaveUserAddress
#         # fields = ["user_id", "addressType", "address", "lat", "lang", "created_at", "updated_at"]
#         fields = ["email", "addressType", "address", "lat", "lang", "created_at", "updated_at"]

#         #fields = ["id", "address", "lat", "lang"]


    