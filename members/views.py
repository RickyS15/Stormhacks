from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializer import MemberSerializer
from .models import Member

# Create your views here.

class MemberAPI(APIView):
    def post(self, request): 
        members = MemberSerializer(data=request.data)
        if members.is_valid():
            members.save()
            return Response(memebers.data)
        return Response(members.errors)

    def get(self, request):
        mem = Member.objects.all()

        serializer = MemberSerializer(mem, many=True)

        return Response(serializer.data)
    