# Generated by Django 4.0.6 on 2022-11-22 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0062_remove_vist_zapisiv_vist_zanv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vist',
            old_name='enddate',
            new_name='eventdate',
        ),
        migrations.RemoveField(
            model_name='vist',
            name='startdate',
        ),
    ]