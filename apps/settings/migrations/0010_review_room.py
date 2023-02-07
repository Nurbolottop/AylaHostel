# Generated by Django 4.1.5 on 2023-02-06 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
        ('settings', '0009_review_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='room',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='room_review', to='rooms.room', verbose_name='Комната'),
            preserve_default=False,
        ),
    ]
