# Generated by Django 4.1.5 on 2023-03-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='О нас')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.AlterModelOptions(
            name='weare',
            options={'verbose_name': 'Где мы есть?', 'verbose_name_plural': 'Где мы есть?'},
        ),
    ]
