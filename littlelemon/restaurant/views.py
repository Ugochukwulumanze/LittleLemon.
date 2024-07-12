from rest_framework.decorators import api_view
from .models import Menu,Booking,User
from rest_framework import generics
from .serializers  import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated




# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
   