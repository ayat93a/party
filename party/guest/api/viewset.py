from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from guest.models import Guest
from .serializers import Guestserializers
from rest_framework.permissions import IsAuthenticated
from .permissions import ISOwnerOrReader


class GuestListAPIView(ListAPIView):
    serializer_class = Guestserializers
    queryset = Guest.objects.all()
   


class GuestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Guestserializers
    queryset = Guest.objects.all()
    permission_classes = (ISOwnerOrReader , IsAuthenticated,)
    