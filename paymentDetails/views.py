from rest_framework.response import Response
from rest_framework import status
from rest_framework. views import APIView
from . payment_serializer import pamentSerializer 
from . models import Payment_Detils


# Create your views here.

class paymentView(APIView):
    def post(self, request, format=None):
        serializers = pamentSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({'msg': 'Order Placed',}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    


class paymentGet(APIView):
    def get(self,request, format=None):
        model = Payment_Detils.objects.get(payment_transaction_id=self.request.data['payment_transaction_id'])
        serializers = pamentSerializer(model)
        return Response(serializers.data)