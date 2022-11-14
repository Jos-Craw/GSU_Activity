# Generated by Django 4.0.6 on 2022-11-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0032_alter_advuser_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('cult', 'Культурно-досуговая деятельность'), ('sport', 'Спортивная деятельность'), ('mass', 'Массовые мероприятия и выставки'), ('trud', 'Трудовая и волонтерская деятельность')], max_length=50, null=True),
        ),
    ]