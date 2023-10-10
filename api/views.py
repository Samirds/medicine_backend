from django.shortcuts import render
from . models import Product_Information
from .api_serializers import Product_Info_serializer, combine
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.


class Product_Info_View(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    # def get(self,request, format=None):
    #     serializers = Product_Info_serializer(data=request.data)
    #     if serializers.is_valid():
    #         return Response(serializers.data)
        
    #     return Response({"Something is Wrong"})

    def get(self,request, format=None):
        model = Product_Information.objects.all()
        serializers = Product_Info_serializer(model, many=True)
        no_of_prod = Product_Information.objects.count()
        
        return Response( {"total_size" : no_of_prod, "ProductsModel": serializers.data})
        
    



class comb(APIView):
    def get(self,request, format=None):
        model1 = Product_Information.objects.all()
        serializers = combine(many=True)
        return Response(serializers.data)
