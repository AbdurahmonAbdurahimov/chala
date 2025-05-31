from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')
