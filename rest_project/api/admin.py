from django.contrib import admin 
from .models import * 
 
 
class OrderTourAdmin(admin.ModelAdmin): 
    """ 
    Параметры для админ панели модели Заказа туров 
    """ 
    list_display = ('individual_number', 'customer_name', 'phone_number', 'chosen_tour', 'date', 
                    'tourists', 'order_bill', 'chosen_car', 'questions', 'order_time', 
                    'company_confirmed', 'actual', 'is_done') 
    list_filter = ('company_confirmed', 'actual', 'is_done') 
 
 
class ReplicaAdmin(admin.ModelAdmin): 
    """ 
    Параметры для админ панели модели Реплик 
    """ 
    list_display = ('name', 'var', 'kaz', 'rus', 'eng') 
 
 
class CaravanSarayAdmin(admin.ModelAdmin): 
    """ 
    Параметры для админ панели модели Караван сарая 
    """ 
    list_display = ('name', 'var', 'kaz', 'rus', 'eng') 
 
 
class OrderCampingAdmin(admin.ModelAdmin): 
    """ 
    Параметры для админ панели модели  
    """ 
    list_display = ('name', 'var', 'kaz', 'rus', 'eng') 
 
admin.site.register(OrderTour, OrderTourAdmin) 
admin.site.register(Replica, ReplicaAdmin) 
admin.site.register(OrderCamping) 
admin.site.register(CaravanSaray) 
admin.site.register(Tour)