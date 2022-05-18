# Generated by Django 4.0.4 on 2022-05-16 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sparrow_app', '0003_alter_list_follow_options_alter_message_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('bday', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('regdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Registro')),
                ('profilepic', models.ImageField(upload_to='', verbose_name='Imagen de perfil')),
                ('bgColor', models.CharField(max_length=15, verbose_name='Color de Fondo')),
                ('txtColor', models.CharField(max_length=15, verbose_name='Color de Texto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.AlterField(
            model_name='list_follow',
            name='id_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Siguiendo', to=settings.AUTH_USER_MODEL, verbose_name='Id de Seguidor'),
        ),
        migrations.AlterField(
            model_name='list_follow',
            name='id_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seguidor', to=settings.AUTH_USER_MODEL, verbose_name='Id de Usuario'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID de usuario'),
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
