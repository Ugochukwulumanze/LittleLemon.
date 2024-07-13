from rest_framework.decorators import api_view
from .models import Menu,Booking,User
from rest_framework import generics
from .serializers  import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render




# Create your views here. 
def index(request):
    return render(request, 'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
   