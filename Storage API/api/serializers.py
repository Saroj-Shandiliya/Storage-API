#Here we convert the django database models to JSon 
from rest_framework import serializers
from .models import item,location

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=item
        fields=('__all__')

class locationSerializers(serializers.ModelSerializer):
    class Meta:
        model=location
        fields=('__all__')
