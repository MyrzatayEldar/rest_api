from rest_framework import serializers 
from .models import * 
 
 
class ReplicaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Replica 
        fields = ['name', 'var', 'kaz', 'rus', 'eng']


class OrderTourSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = OrderTour 
        fields = '__all__'
