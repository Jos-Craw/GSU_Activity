# Generated by Django 4.0.6 on 2022-11-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0049_consult_zan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='eventtime',
            field=models.CharField(choices=[('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00')], max_length=10),
        ),
    ]
