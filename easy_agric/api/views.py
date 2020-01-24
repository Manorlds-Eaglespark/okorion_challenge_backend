# views.py
import json
from rest_framework.views import APIView, Response
from .serializers import DistrictDateSerializer
from .models import DistrictDate
from rest_framework.permissions import AllowAny




class MyOwnView(APIView):
    def get(self, request):
        permission_classes = (AllowAny)
        with open('interview.json') as f:
            data = json.loads(f.read())
            serializer = DistrictDateSerializer(data, many=True)
            return Response({"data":serializer.data})