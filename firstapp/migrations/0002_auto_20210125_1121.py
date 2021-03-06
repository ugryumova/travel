# Generated by Django 3.1.5 on 2021-01-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='id_punkt',
        ),
        migrations.RemoveField(
            model_name='price_list',
            name='id_punkt',
        ),
        migrations.RemoveField(
            model_name='price_list',
            name='id_transport_type',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='id_hotel',
        ),
        migrations.AddField(
            model_name='price_list',
            name='id_hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.hotel'),
        ),
    ]
