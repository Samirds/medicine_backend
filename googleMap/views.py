<<<<<<< HEAD
# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework. views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from . serializers import userSerializers, saveUserAddressSerialiser
# import requests
# from .models import SaveUserAddress

# # Create your views here.


# class getLatLang(APIView):   #this method should not be followed correct way is class getAddressList(APIView)
#     def post(self, request, format=None):
#         serializers = userSerializers(data = request.data)
#         if serializers.is_valid():
#             res = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='
#                                +serializers["lat"].value+', '
#                                +serializers["lang"].value+
#                                '&key='+"AIzaSyCwyUkHyJh6exkjkrYHRwWpUSslSklp3YQ")
=======
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework. views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import userSerializers, saveUserAddressSerialiser
import requests
from .models import SaveUserAddress

# Create your views here.


class getLatLang(APIView):   #this method should not be followed correct way is class getAddressList(APIView)
    def post(self, request, format=None):
        serializers = userSerializers(data = request.data)
        if serializers.is_valid():
            res = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='
                               +serializers["lat"].value+', '
                               +serializers["lang"].value+
                               '&key='+"API KEY")
>>>>>>> 85e7e95fc2d37e61710daa51e27f8710fbaa9642
           
#             #return Response(res, status = status.HTTP_200_OK)
#             return HttpResponse(res)
#         return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        
      



# class saveUserAddressView(APIView):
#     def post(self, request, format=None):
#         # obj, created = SaveUserAddress.objects.update_or_create(user_id=self.request.data['user_id'], defaults=request.data)
#         obj, created = SaveUserAddress.objects.update_or_create(email=self.request.data['email'], defaults=request.data)
#         print("obj is {}".format(obj))
#         print("created is {}".format(created))

#         serializers = saveUserAddressS
#         erialiser(data=request.data)
#         if serializers.is_valid():
#             print("\n valid \n")
#             #serializers.save()
#             if created:
#                 return Response({'message': 'User address save Succesfully'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'message': 'User address updated Succesfully'}, status=status.HTTP_200_OK)
            
#         else:
#             print("\n\n not valid \n\n")
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





# class getAddressList(APIView):   #this method should follow
#     def post(self,request, format=None):
#         model = SaveUserAddress.objects.filter(email=self.request.data['email'])
#         serializers = saveUserAddressSerialiser(model, many=True)
#         return Response({"message": serializers.data}, status=status.HTTP_200_OK)


    


