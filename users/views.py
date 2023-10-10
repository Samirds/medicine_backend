from rest_framework.response import Response
from rest_framework import status
from rest_framework. views import APIView
from .user_serializers import RegistrationSerializers, LoginSerializer, userSerialization
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from . models import CustomUser



# Create your views here.


class Registration(APIView):
    def post(self, request, format=None):
        serializers = RegistrationSerializers(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({'msg': 'Registration Succesfull',}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    

# ----------------------------------------------- Its for Generating Tokens ---------------------------------------------
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# ------------------------------------------------------------------------------------------------------------------


class Login(APIView):
    def post(self, request, format=None):
        serializers = LoginSerializer(data=request.data, )
        if serializers.is_valid():
            
            email = serializers.data.get('email')
            password = serializers.data.get('password')

            user = authenticate(email = email, password = password)
           
            if user is not None:
            #serializers.save()
                login(request, user)
                token = get_tokens_for_user(user)
                first_name = user.first_name
                last_name = user.last_name
                user_email = user.email
                gender = user.gender
                age = user.age
                pincode = user.pincode
                address = user.address
                return Response({'first_name' : first_name, "Last": last_name, "email": user_email, "Gender": gender,"age":age, "pincode": pincode,"address": address, "tokens": token},
                        status=status.HTTP_200_OK)
            return Response({"Email or Password is not exist in admin panel"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED,)
    



# class Profile(APIView):

#     def get(self, request, format=None):
#         serializers = ProfileSerializer(data=request.user)
#         if serializers.is_valid():
        
#             return Response(serializers.data,
#                             status=status.HTTP_200_OK)
        
#         return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)

class Profile(APIView):

    def get(self,request, format=None):
        model = CustomUser.objects.all()
        serializers = userSerialization(model, many=True)
        return Response(serializers.data)

    


