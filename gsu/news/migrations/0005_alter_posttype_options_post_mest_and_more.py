# Generated by Django 4.0.6 on 2022-12-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_group_posttype_zap_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posttype',
            options={'verbose_name': 'Запись мероприяти', 'verbose_name_plural': 'Записи мероприятий'},
        ),
        migrations.AddField(
            model_name='post',
            name='mest',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='mesta_now',
            field=models.IntegerField(null=True, verbose_name='Количество мест сейчас'),
        ),
    ]
