# Generated by Django 4.0.6 on 2022-12-05 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0078_alter_post_mesta_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mesta_now',
            field=models.IntegerField(default=2, null=True, validators=[django.core.validators.MaxValueValidator(models.IntegerField(default=2, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество мест всего'))], verbose_name='Количество мест сейчас'),
        ),
    ]
