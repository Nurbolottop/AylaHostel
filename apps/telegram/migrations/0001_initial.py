# Generated by Django 4.1.5 on 2023-02-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_telegram', models.PositiveBigIntegerField(verbose_name='ID телеграм')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Пользователь телеграмма',
                'verbose_name_plural': 'Пользователи телеграмма',
            },
        ),
    ]