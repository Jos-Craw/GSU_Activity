# Generated by Django 4.0.6 on 2022-11-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0060_remove_vist_pdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vist',
            old_name='eventdate',
            new_name='enddate',
        ),
        migrations.AddField(
            model_name='vist',
            name='startdate',
            field=models.DateField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='vist',
            name='eventtime',
            field=models.CharField(choices=[('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00')], max_length=10),
        ),
    ]