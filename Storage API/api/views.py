from rest_framework import generics

from .models import item,location
from .serializers import ItemSerializers,locationSerializers

class itemList(generics.ListCreateAPIView):
    serializer_class=ItemSerializers

    def get_queryset(self):
        queryset=item.objects.all()
        location=self.request.query_params.get('location')
        if location is not None:
            queryset= queryset.filter(itemLocation=location)
        return queryset

class itemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ItemSerializers
    queryset=item.objects.all()

class locationList(generics.ListCreateAPIView):
    serializer_class=locationSerializers
    queryset=location.objects.all()

class locationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=locationSerializers
    queryset=location.objects.all()