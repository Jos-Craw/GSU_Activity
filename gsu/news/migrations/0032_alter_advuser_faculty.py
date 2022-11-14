# Generated by Django 4.0.6 on 2022-11-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_advuser_faculty_advuser_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='faculty',
            field=models.CharField(blank=True, choices=[('bio', 'Биологический факультет'), ('geo', 'Геолого-географический факультет'), ('ist', 'Факультет истории и межкультурных коммуникаций'), ('in', 'Факультет иностранных языков'), ('mat', 'Факультет математитики и ТП'), ('psi', 'Факультет психологии и педагогики'), ('fiz', 'Факультет физики и ИТ'), ('ffk', 'Факультет физической культуры'), ('fil', 'Филологический факультет'), ('eko', 'Экономический факультет'), ('yr', 'Юридичесий факультет')], max_length=50, null=True),
        ),
    ]