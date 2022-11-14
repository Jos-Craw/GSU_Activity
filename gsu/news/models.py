from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification
import os


class AdvUser(AbstractUser):
    fac = (
        ('bio','Биологический факультет'),
        ('geo','Геолого-географический факультет'),
        ('ist','Факультет истории и межкультурных коммуникаций'),
        ('in','Факультет иностранных языков'),
        ('mat','Факультет математитики и ТП'),
        ('psi','Факультет психологии и педагогики'),
        ('fiz','Факультет физики и ИТ'),
        ('ffk','Факультет физической культуры'),
        ('fil','Филологический факультет'),
        ('eko','Экономический факультет'),
        ('yr','Юридичесий факультет'),
        )
        

    is_activated = models.BooleanField(default=True, db_index=True,verbose_name='Прошел активацию?')
    avatar = models.ImageField(null=True, blank=True, upload_to="image/profile/")
    phone_num = models.CharField(unique = True, null = True, blank = False, max_length=13)
    faculty = models.CharField(null = True, blank = True,choices=fac,max_length=50)
    group = models.CharField(null = True, blank = True,max_length=10)



    class Meta(AbstractUser.Meta):
        pass


class Post(models.Model):
    tag = (
        ('cult','Культурно-досуговая деятельность'),
        ('sport','Спортивная деятельность'),
        ('mass','Массовые мероприятия и выставки'),
        ('trud','Трудовая и волонтерская деятельность'),
        )

    content = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, null=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True)
    video = models.FileField(upload_to='video/%Y/%m/%d/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/%Y/%m/%d/', blank=True, null=True)
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True)
    pubdate = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Publication date')
    eventtime = models.TimeField(db_index=True,null=True,blank=False)
    eventdate = models.DateField(db_index=True,null=True,blank=False)
    stoim = models.CharField(null = True, blank = False, max_length=10)
    mesta = models.CharField(null = True, blank = False, max_length=10)
    tags = models.CharField(null = True, blank = False,choices=tag, max_length=50)
    zapisi = models.ManyToManyField(AdvUser, related_name='Записаные',blank=True)

    class Meta:
        verbose_name_plural = 'События'
        verbose_name = 'Событие'
        ordering = ['-pubdate']

    def filename(self):
        return os.path.basename(self.file.name)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True, blank=False)
    author = models.CharField(max_length=30)
    pubdate = models.DateTimeField(auto_now_add=True, db_index=True)
    moderation = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        ordering = ['-pubdate']


user_registrated = Signal(['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)
