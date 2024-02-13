from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

LOCATION_CHOICES = {
    'BISHKEK': 'Бишкек',
    'TOKMOK': 'Токмок',
    'BOSTERY': 'Бостери',
    'BALYKCHY': 'Балыкчы'
}

CURRENCY_CHOICES = {
        'DOLLAR': 'Доллар USA',
        'SOM': 'Сом'
    }



class Auto(models.Model):
    
    TYPE_OF_BODY_CHOICES = {
        'SEDAN': 'Седан',
        'HATCHBACK': 'Хетчбек',
        'UNIVERSAL': 'Универсал',
        'CROSSOVER': 'Кроссовер',
        'SUV': 'Внедорожник',
        'CABRIOLET': 'Кабриолет'
    }

    TRANSMISSION_CHOICES = {
        'MECHANICS': 'Механика',
        'AUTOMAT': 'Автомат'
    }

    WHEEL_CHOICES = {
        'LEFT': 'Левый',
        'RIGTH': 'Правый',
    }

    CONDITIONS_CHOICES = {
        'GOOD': 'Хорошее',
        'EXCELLENT': 'Идеальное',
        'EMERGENCY': 'Не на ходу',
        'NEW': 'Новое'
    }


    AVAILABILITY_CHOICES = {
        'IN_STOCK': 'В Наличии',
        'TO_ORDER': 'На заказ',
        'ON_THE_WAY':'В пути'
    }

    CAR_EXCHANGE_CHOICES = {
        'YES': 'Да',
        'NO': 'Нет'
    }


    mark = models.CharField(verbose_name='Марка', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    year = models.IntegerField(verbose_name='Год',validators=[MinValueValidator(1940)],help_text='Введите год выпуска автомобиля') 
    type_of_body = models.CharField(verbose_name='Тип кузова', max_length=15, choices=TYPE_OF_BODY_CHOICES)
    transmission = models.CharField(verbose_name='Коробка передач', max_length=15, choices=TRANSMISSION_CHOICES)
    wheel = models.CharField(verbose_name = 'Руль', max_length=10, choices=WHEEL_CHOICES)
    color = models.CharField(verbose_name='Цвет', max_length=50)
    condition = models.CharField(verbose_name='Состояние', max_length=20, choices=CONDITIONS_CHOICES)
    mileage = models.IntegerField(verbose_name='Пробег', validators=[MinValueValidator(0)])
    photo = models.ImageField(upload_to='auto_photos/', null=True, blank=True)
    price_currency = models.CharField(verbose_name='Цена в', max_length=20, choices=CURRENCY_CHOICES)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    availability = models.CharField(verbose_name='Наличие', max_length=20, choices=AVAILABILITY_CHOICES)
    car_exchange = models.CharField(verbose_name='Возможность обмена', max_length=20, choices=CAR_EXCHANGE_CHOICES)
    location = models.CharField(verbose_name='локация', max_length=100, choices=LOCATION_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mark}, {self.model}, {self.year}, {self.price}'
    

class House(models.Model):

    NUMBER_OF_ROOMS = {
        '1 ROOM': '1 КОМНАТА',
        '2 ROOMS': '2 КОМНАТЫ',
        '3 ROOMS': '3 КОМНАТЫ',
        '4 ROOMS': '4 КОМНАТЫ',
        '5 ROOMS': '5 КОМНАТЫ',
        '6 ROOMS': '6 КОМНАТЫ',
        '7 ROOMS': '7 КОМНАТЫ',
    }

    YEAR_OF_BUILDINGS = {
        'UNTILL 19650': 'До 1950',
        '1950-1959': '1950-1959',
        '1960-1969': '1960-1969',
        '1970-1979': '1970-1979',
        '1980-1989': '1980-1989',
        '1990-1999': '1990-1999',
        '2000-2009': '2000:2009',
        '2010-2019': '2010-2019',
        '2020-current': '2020-наст.время'

    }

    TYPE_OF_HOUSE_CHOICES = {
        'APPARTMENT': 'КВАРТИРА',
        'COMMERCIAL_ESTATE': 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ',
        'PRIVATE HOUSE': 'ЧАСТНЫЙ ДОМ'
    }

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Недвижимость', max_length=100, choices=TYPE_OF_HOUSE_CHOICES)
    location = models.CharField(verbose_name='локация', max_length=100, choices=LOCATION_CHOICES)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    price_currency = models.CharField(verbose_name='Цена в', max_length=20, choices=CURRENCY_CHOICES)
    number_of_rooms = models.CharField(verbose_name='Количество комнат',max_length=100, choices=NUMBER_OF_ROOMS)
    square = models.IntegerField(verbose_name='Площадь(м2)')
    floor = models.IntegerField(verbose_name='Этаж', validators=[MinValueValidator(1), MaxValueValidator(15)])
    year_of_buildings = models.CharField(verbose_name='Год постройки', max_length=100, choices=YEAR_OF_BUILDINGS)

    def __str__(self):
        return self.name