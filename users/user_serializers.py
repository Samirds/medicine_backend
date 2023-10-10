from imaplib import _Authenticator
from rest_framework import serializers

from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login






#---------------------------------------------------- AUTHENTICATION ---------------------------------------------------

# ----------------------------------------   REGISTER -----------------------------------------------------
class RegistrationSerializers(serializers.ModelSerializer):
    #pincode = serializers.IntegerField(required=False,)
    class Meta:
        # password2 = serializers.CharField(style={
        #     'input_type': 'password'
        # }, write_only=True)
        model = CustomUser
        fields  =  ["first_name", "last_name", "gender", "age",  "password", "email", "pincode", "address"]
        # extra_kwargs = {
        #     'password': {'write_only':True}
        # }


    def validate(self, data):
         
         email = data.get('email').strip().lower()
         if CustomUser.objects.filter(email=email).exists():
            #raise serializers.ValidationError('User with this email id already exist.')
            raise ValidationError("dumb")
            

         password = data.get("password")
         special_charecter = ["@", "&", "#", "$", "%", "_"]

         if (len(password) >= 8 and  bool(any(i in password for i in special_charecter))):
            return data
         else:
          raise ValidationError("Password must have a symbol and total length of 8")
         

    def create(self, validated_data):  # here we are using custome user mdoel so we have to override the create method
        user = CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'], first_name=validated_data['first_name'], age=validated_data['age'], gender=validated_data['gender'], last_name=validated_data['last_name'], address=validated_data['address'], pincode=validated_data['pincode'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------  Log In    -------------------------------------------------------------------------------------------------------

    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50, style={'input_type': 'password'}, trim_whitespace=False)
    class Meta:
        model = CustomUser
        fields = ["email", "password"]




class userSerialization(serializers.ModelSerializer):
 
    class Meta:
        model = CustomUser
        
        fields = '__all__'


