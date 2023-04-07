# Generated by Django 4.1.5 on 2023-04-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_setting_instagram_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefit',
            name='description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='description_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]