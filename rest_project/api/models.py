from django.db import models 
import uuid 


class_type_choices_rus = ( 
    ('стандарт', 'стандарт'), 
    ('стандарт плюс', 'стандарт плюс'), 
    ('эконом', 'эконом'), 
    ('люкс', 'люкс') 
) 
 
class Replica(models.Model): 
    name = models.CharField(max_length=20, verbose_name='Описание переменной') 
    var = models.CharField(max_length=20, verbose_name='Переменная в которой нужно хранить') 
    kaz = models.TextField(verbose_name='Казахская реплика') 
    rus = models.TextField(verbose_name='Русская реплика') 
    eng = models.TextField(verbose_name='Английская реплика') 
     
    def __str__(self): 
        return self.name 
     
    class Meta: 
        verbose_name = "Реплика" 
        verbose_name_plural = "Реплики" 
 
 
class OrderTour(models.Model): 
    individual_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Уникальный номер') 
    customer_name = models.CharField(max_length=60, verbose_name='Имя заказчика') 
    phone_number = models.CharField(max_length=12, null=True, verbose_name='Номер телефона') 
    chosen_tour = models.CharField(max_length=100, null=True, verbose_name='Выбранный тур') 
    date = models.CharField(max_length=50, null=True, verbose_name='Дата тура') 
    tourists = models.IntegerField(null=True, verbose_name='Туристов') 
    order_bill = models.FloatField(null=True, verbose_name='Счет за тур') 
    chosen_car = models.CharField(max_length=100, null=True, verbose_name='Выбранный транспорт') 
    questions = models.TextField(null=True, verbose_name='Вопросы к туру') 
    order_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время заказа') 
    company_confirmed = models.BooleanField(default=False, null=True, verbose_name='Подтверждено компанией') 
    actual = models.BooleanField(default=False, null=True, verbose_name='Актуально') 
    is_done = models.BooleanField(default=False, null=True, verbose_name='Исполнено') 
     
    def __str__(self): 
        return f"Заказ {self.customer_name} - {self.chosen_tour}" 
 
    class Meta: 
        verbose_name = "Заказ по туру" 
        verbose_name_plural = "Заказы по туру" 
 
     
class CaravanSaray(models.Model): 
    name = models.CharField(max_length=50, verbose_name='Имя кемпинга') 
    class_type = models.CharField(choices=class_type_choices_rus, max_length=20, verbose_name='Класс') 
    beds = models.CharField(max_length=10, verbose_name='Количество кроватей') 
    price_per_1_night = models.FloatField(null=True, verbose_name='Цена за 1 ночь', blank=True) 
    price_per_2_nights = models.FloatField(null=True, verbose_name='Цена за 2 ночи', blank=True) 
    price_per_3_nights = models.FloatField(null=True, verbose_name='Цена за 3 ночи', blank=True) 
    price_per_4_nights = models.FloatField(null=True, verbose_name='Цена за 4 ночи', blank=True) 
    price_per_5_nights = models.FloatField(null=True, verbose_name='Цена за 5 ночей', blank=True) 
    is_occupied = models.BooleanField(default=False, verbose_name='Занято', null=True) 
     
    def __str__(self): 
        return f"Кемпинг {self.name} - класс: {self.class_type}" 
 
    class Meta: 
        verbose_name = 'Караван Сарай' 
        verbose_name_plural = 'Караван Сараи' 
     
 
class OrderCamping(models.Model): 
    individual_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Уникальный номер') 
    name = models.CharField(max_length=100, verbose_name='Имя клиента') 
    caravan = models.ForeignKey('CaravanSaray', on_delete=models.CASCADE, verbose_name='Выбранный караван') 
    guests = models.IntegerField(verbose_name='Количество гостей') 
    date_arrange = models.CharField(max_length=100, verbose_name='Диапазон даты') 
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона') 
    company_confirmed = models.BooleanField(default=False, null=True, verbose_name='Подтверждено компанией') 
    actual = models.BooleanField(default=False, null=True, verbose_name='Актуально') 
    is_done = models.BooleanField(default=False, null=True, verbose_name='Исполнено')
     
    def __str__(self): 
        return f"Заказ на имя {self.name} - караван: {self.caravan}" 
 
    class Meta: 
        verbose_name = 'Заказ по брони кемпинга' 
        verbose_name_plural = 'Заказы по брони кемпинга' 
 
 
class Tour(models.Model): 
    name = models.CharField(max_length=100, verbose_name='Название тура') 
    car = models.CharField(max_length=100, verbose_name='Автомашина') 
    distance = models.FloatField(verbose_name='Расстояние') 
    bought_times = models.IntegerField(verbose_name='Сколько раз куплен') 
 
    def __str__(self): 
        return f"Тур {self.name}" 
     
    class Meta: 
        verbose_name = 'Тур' 
        verbose_name_plural = 'Туры'