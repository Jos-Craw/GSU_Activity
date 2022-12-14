# Generated by Django 4.0.6 on 2022-12-05 17:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventdate', models.DateField(db_index=True, null=True, verbose_name='Дата')),
                ('eventtime', models.CharField(choices=[('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00')], max_length=10, verbose_name='Время')),
                ('zan', models.BooleanField(db_index=True, default=False, verbose_name='Занятость')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
                'ordering': ['eventdate'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtime', models.TimeField(db_index=True, null=True, verbose_name='Время')),
                ('eventdate', models.DateField(db_index=True, null=True, verbose_name='Дата')),
                ('zan', models.BooleanField(db_index=True, default=False, verbose_name='Занято')),
                ('group', models.BooleanField(db_index=True, default=False, verbose_name='Групповая')),
            ],
            options={
                'verbose_name': 'Время и дата выставки',
                'verbose_name_plural': 'Время и дата выставки',
            },
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BooleanField(db_index=True, default=False, verbose_name='Групповая запись')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('otobr', models.BooleanField(db_index=True, default=False, verbose_name='Отображение')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секции',
            },
        ),
        migrations.CreateModel(
            name='Trud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('otobr', models.BooleanField(db_index=True, default=False, verbose_name='Отображение')),
            ],
            options={
                'verbose_name': 'Трудовое направление',
                'verbose_name_plural': 'Трудовые направления',
            },
        ),
        migrations.CreateModel(
            name='Tvor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('otobr', models.BooleanField(db_index=True, default=False, verbose_name='Отображение')),
            ],
            options={
                'verbose_name': 'Творческое направление',
                'verbose_name_plural': 'Творческие направления',
            },
        ),
        migrations.CreateModel(
            name='Volant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('otobr', models.BooleanField(db_index=True, default=False, verbose_name='Отображение')),
            ],
            options={
                'verbose_name': 'Волонтерское направление',
                'verbose_name_plural': 'Волонтерские направления',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['eventdate'], 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.RemoveField(
            model_name='advuser',
            name='send_messages',
        ),
        migrations.AddField(
            model_name='advuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile/', verbose_name='Аватарка'),
        ),
        migrations.AddField(
            model_name='advuser',
            name='faculty',
            field=models.CharField(choices=[('bio', 'Биологический факультет'), ('geo', 'Геолого-географический факультет'), ('ist', 'Факультет истории и межкультурных коммуникаций'), ('in', 'Факультет иностранных языков'), ('mat', 'Факультет математитики и ТП'), ('psi', 'Факультет психологии и педагогики'), ('fiz', 'Факультет физики и ИТ'), ('ffk', 'Факультет физической культуры'), ('fil', 'Филологический факультет'), ('eko', 'Экономический факультет'), ('yr', 'Юридичесий факультет')], max_length=50, null=True, verbose_name='Факультет'),
        ),
        migrations.AddField(
            model_name='advuser',
            name='group',
            field=models.CharField(max_length=10, null=True, verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='advuser',
            name='phone_num',
            field=models.CharField(max_length=13, null=True, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/%Y/%m/%d/', verbose_name='Аудио'),
        ),
        migrations.AddField(
            model_name='post',
            name='eventdate',
            field=models.DateField(db_index=True, null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='post',
            name='eventtime',
            field=models.TimeField(db_index=True, null=True, verbose_name='Время'),
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/', verbose_name='Приклепленные файлы'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='post',
            name='mesta',
            field=models.IntegerField(default=2, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество мест всего'),
        ),
        migrations.AddField(
            model_name='post',
            name='mesta_now',
            field=models.IntegerField(default=2, null=True, validators=[django.core.validators.MaxValueValidator(models.IntegerField(default=2, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество мест всего'))], verbose_name='Количество мест сейчас'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='stoim',
            field=models.CharField(max_length=10, null=True, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('cult', 'Культурно-досуговая деятельность'), ('sport', 'Спортивная деятельность'), ('mass', 'Массовые мероприятия и выставки'), ('trud', 'Трудовая и волонтерская деятельность')], max_length=50, null=True, verbose_name='Тэг'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/%Y/%m/%d/', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='post',
            name='zapis',
            field=models.ManyToManyField(blank=True, related_name='Записаные', through='news.PostType', to=settings.AUTH_USER_MODEL, verbose_name='Записаные'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Vist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('content', models.TextField(null=True, verbose_name='Контент')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d/', verbose_name='Изображение')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/', verbose_name='Приклепленные файлы')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/%Y/%m/%d/', verbose_name='Видео')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/%Y/%m/%d/', verbose_name='Аудио')),
                ('pubdate', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('stoim', models.CharField(max_length=10, null=True, verbose_name='Стоимость')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('event', models.ManyToManyField(blank=True, related_name='Даты', to='news.event', verbose_name='Время и дата')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
                'ordering': ['pubdate'],
            },
        ),
        migrations.AddField(
            model_name='posttype',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.post'),
        ),
        migrations.AddField(
            model_name='posttype',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='zapisi',
            field=models.ManyToManyField(blank=True, related_name='Записи', to=settings.AUTH_USER_MODEL, verbose_name='Записаные'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True, verbose_name='Контент')),
                ('author', models.CharField(max_length=30, verbose_name='Автор')),
                ('pubdate', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='Мероприятие')),
                ('vist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.vist', verbose_name='Выставка')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-pubdate'],
            },
        ),
    ]
