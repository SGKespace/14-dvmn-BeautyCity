from django.db import models

# Create your models here.
class BeautySaloon(models.Model):
    name = models.CharField(
        'Название салона', max_length=200, db_index=True
    )
    address = models.TextField(
        'Адрес салона',
        help_text='ул. Подольских курсантов д.5 кв.4')


class Employee(models.Model):
    name = models.CharField(
        'ФИО Работника', max_length=200, db_index=True
    )

class Serivice(models.Model):
    name = models.CharField(
        'Название услуги', max_length=200, db_index=True
    )
    price= models.FloatField(
        'Стоимость услуги',
    )

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(
        'ФИО Клиента',
        max_length=200
    )
    phonenumber = models.CharField('Номер телефона клиента', max_length=20)

class Schedule(models.Model):
    saloon = models.ForeignKey(
        BeautySaloon,
        on_delete=models.SET_NULL,
        related_name='schedules',
        verbose_name='Салон',
        null=True,
        blank=False
    )

    service = models.ForeignKey(
        Serivice,
        on_delete=models.SET_NULL,
        related_name='schedules',
        verbose_name='Услуга',
        null=True,
        blank=False
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        related_name='schedules',
        verbose_name='Покупатель',
        null=True,
        blank=False
    )

    created_at = models.DateTimeField(
        'Дата время создания записи',
        null = True,
        blank = False
    )

    start_at = models.DateTimeField(
        'Начало сеанса',
        null = True,
        blank = False
    )
    end_at = models.DateTimeField(
        'Окончание сеанса',
        null = True,
        blank = False
    )

    price= models.FloatField(
        'Стоимость услуги',
        null = True,
        blank = False
    )

    deliver = models.BooleanField(
        'Услуга оказана',
        null = True,
        blank = False,
        default=False
    )

    tentatively = models.BooleanField(
        'Предварительная запись',
        null = True,
        blank = False,
        default=True
    )