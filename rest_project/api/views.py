from django.shortcuts import render 
from django.http import HttpResponse 
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request): 
    return render(request=request, template_name='templates/index.html', context={}) 
 
 
def home(request): 
    return HttpResponse('<h1>Hello world!</h1>')


class ReplicaListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Получение всех реплик
        '''
        replicas = Replica.objects.all()
        serializer = ReplicaSerializer(replicas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Добавление реплик в базу данных
        '''
        data = {
            'name': request.data.get('name'), 
            'var': request.data.get('var'), 
            'kaz': request.data.get('kaz'),
            'rus': request.data.get('rus'),
            'eng': request.data.get('eng')
        }
        serializer = ReplicaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderTourListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Получить все заказанные туры
        '''
        ordered_tours = OrderTour.objects.all()
        serializer = OrderTourSerializer(ordered_tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Сделать заказ по туру
        '''
        data = {
            'customer_name': request.data.get('customer_name'), 
            'phone_number': request.data.get('phone_number'), 
            'chosen_tour': request.data.get('chosen_tour'),
            'date': request.data.get('date'),
            'tourists': request.data.get('tourists'),
            'order_bill': request.data.get('order_bill'), 
            'chosen_car': request.data.get('chosen_car'), 
            'questions': request.data.get('questions')
        }
        serializer = OrderTourSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
