# Generated by Django 4.0.6 on 2022-11-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0048_alter_consult_eventtime_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='zan',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Занято?'),
        ),
    ]
