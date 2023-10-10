from . models import PrescriptionImage
from . ImageUploadSerializer import Image_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# # Create your views here.

class UploadImage(APIView):
    def post(self, request, format=None):
        serializers = Image_serializer(data=request.data)#, files = request.FILES)
        if serializers.is_valid():
            serializers.save()
            print("\n\nhere is serializer is safe");
    
            return Response({'msg': 'Image Upload Succesfully'}, status=status.HTTP_200_OK)

        print("\n\nhere is serializer is not safe");
        print("\n ",serializers.errors)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShowUploadedImage(APIView):
    def get(self,request, format=None):
        model = PrescriptionImage.objects.all()
        serializers = Image_serializer(model, many=True)
        return Response( serializers.data)
    