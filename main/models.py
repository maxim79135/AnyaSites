from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    surname = models.CharField('Фамилия',max_length=30)
    name = models.CharField('Имя',max_length=30)
    middle_name = models.CharField('Отчество',max_length=30)
    birthday = models.DateField('Дата рождения')
    phone = models.DecimalField('Телефон',max_digits=11,decimal_places=0)
    #password = models.DecimalField('Пароль', max_digits=10, decimal_places=0)

    def __str__(self):
        return self.surname


class Marathon(models.Model):
    title = models.CharField('Название',max_length=30)
    season = models.DecimalField('Сезон',max_digits=3,decimal_places=0)
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата конца')

    def __str__(self):
        return self.title

class Contract(models.Model):
    date = models.DateField('Дата')
    marathon = models.ForeignKey(Marathon, null=True, on_delete=models.PROTECT, verbose_name='Марафон')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Клиент')

    def __str__(self):
        return str(self.date)


class Lection(models.Model):
    title = models.CharField('Название', max_length=30)
    date = models.DateField('Дата')
    description = models.TextField('Описание')
    video = models.CharField('Видео', max_length=500)
    marathon = models.ForeignKey(Marathon, null=True, on_delete=models.PROTECT, verbose_name='Марафон')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/lection'


class Post(models.Model):
    title = models.CharField('Название', max_length=30)
    date = models.DateField('Дата')
    description = models.TextField('Описание')
    # img = models.ImageField('Изображение',default="no_image.jpg", upload_to='static')
    img = models.CharField('Видео', max_length=500)
    marathon = models.ForeignKey(Marathon, null=True, on_delete=models.PROTECT, verbose_name='Марафон')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/lection'

class Diary(models.Model):
    title = models.CharField('Название',max_length=30)
    date = models.DateField('Дата')
    breakfast = models.TextField('Завтрак', null=True, blank=True)
    lunch = models.TextField('Обед', null=True, blank=True)
    dinner = models.TextField('Ужин', null=True, blank=True)
    snack = models.TextField('Перекус', null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    marathon = models.ForeignKey(Marathon, on_delete=models.PROTECT, verbose_name='Марафон')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Клиент')
    #client = models.ForeignKey(Client, null=True, on_delete=models.PROTECT, verbose_name='Клиент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/diary'

class Parameter(models.Model):
    height = models.FloatField('Рост')
    weight = models.FloatField('Вес')
    girth_breast = models.FloatField('Обхват груди')
    girth_waist = models.FloatField('Обхват талии')
    girth_hips = models.FloatField('Обхват бёдер')
    girth_shoulders = models.FloatField('Обхват плеч')
    girth_arm = models.FloatField('Обхват руки')
    girth_leg = models.FloatField('Обхват ноги')
    date = models.DateField('Дата замеров')
    user = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name='Клиент')
    #client = models.ForeignKey(Client, null=True, on_delete=models.PROTECT, verbose_name='Клиент')
    marathon = models.ForeignKey(Marathon, null=True, on_delete=models.PROTECT, verbose_name='Марафон')

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return f'/parameter'

class Workout(models.Model):
    title = models.CharField('Название', max_length=30)
    date = models.DateField('Дата')
    description = models.TextField('Описание')
    video = models.CharField('Видео', max_length=500)
    marathon = models.ForeignKey(Marathon, null=True, on_delete=models.PROTECT, verbose_name='Марафон')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/workout'



