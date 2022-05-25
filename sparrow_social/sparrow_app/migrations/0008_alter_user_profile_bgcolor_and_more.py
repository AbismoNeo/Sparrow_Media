# Generated by Django 4.0.4 on 2022-05-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparrow_app', '0007_alter_message_image_alter_user_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='bgColor',
            field=models.CharField(choices=[], default='Blanco', max_length=15, verbose_name='Color de Fondo'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='txtColor',
            field=models.CharField(choices=[], default='Negro', max_length=15, verbose_name='Color de Texto'),
        ),
    ]
