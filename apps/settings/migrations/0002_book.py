# Generated by Django 4.1.5 on 2023-02-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
    ]
