# Generated by Django 4.0.6 on 2022-12-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_vist_final_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='vist',
            name='start_date',
            field=models.DateField(db_index=True, null=True, verbose_name='Начало выставки'),
        ),
        migrations.AlterField(
            model_name='vist',
            name='final_date',
            field=models.DateField(db_index=True, null=True, verbose_name='Конец выставки'),
        ),
    ]