from rest_framework.response import Response
from rest_framework import status
from rest_framework. views import APIView
from . models import Order_Details
from . order_serializer import orderSerializer



# Create your views here.

class order_View(APIView):
    def post(self, request, format=None):
        serializers = orderSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({'msg': 'Order Placed',}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    



# class order_View_Get(APIView):
#     def get(self,request, format=None):
#         model = Order_Details.objects.filter(user_email=self.request.data['user_email'])
#         serializers = orderSerializer(model, many=True)
#         return Response(serializers.data)




class order_View_Get(APIView):

    def get_queryset(self):
        Email = Order_Details.objects.all()
        return Email
    

    def get(self, request, *args, **kwargs):
        try:
            user_email = request.query_params["user_email"]
            if user_email != None:
                model = Order_Details.objects.get(user_email=user_email)
                serializer = orderSerializer(model)
                
        except:
            email = self.get_queryset()
            serializer = orderSerializer(email, many=True)

        return Response(serializer.data)