# Generated by Django 4.0.6 on 2022-11-21 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0058_alter_post_name_vist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vist',
            options={'verbose_name': 'Выставка', 'verbose_name_plural': 'Выставки'},
        ),
        migrations.RenameField(
            model_name='vist',
            old_name='pubdate',
            new_name='pdate',
        ),
    ]