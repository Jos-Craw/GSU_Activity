# Generated by Django 4.0.6 on 2022-11-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0029_rename_phonenumber_advuser_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='phone_num',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
    ]
