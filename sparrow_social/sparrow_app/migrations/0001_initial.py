# Generated by Django 4.0.4 on 2022-05-11 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('bday', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('username', models.CharField(max_length=20, verbose_name='Usuario')),
                ('password', models.CharField(max_length=15, verbose_name='Contraseña')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('regdate', models.DateTimeField()),
                ('profilepic', models.ImageField(upload_to='')),
                ('bgColor', models.CharField(max_length=15, verbose_name='Color de Fondo')),
                ('txtColor', models.CharField(max_length=15, verbose_name='Color de Texto')),
                ('lastlog', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datepost', models.DateTimeField()),
                ('Text', models.TextField(max_length=150, verbose_name='Mensaje')),
                ('Image', models.ImageField(upload_to='')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sparrow_app.users')),
            ],
        ),
        migrations.CreateModel(
            name='list_follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_friend', models.CharField(max_length=20)),
                ('follow_date', models.DateTimeField()),
                ('id_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sparrow_app.users')),
            ],
        ),
    ]