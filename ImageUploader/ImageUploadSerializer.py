from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import PrescriptionImage



class Image_serializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = PrescriptionImage
        #fields = ['Username', 'UserId',"image"]
        fields = ['Username', "user_email", "uploaded_at", "image"]
       
        

