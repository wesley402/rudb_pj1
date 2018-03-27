# Generated by Django 2.0.3 on 2018-03-24 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('zip_code', models.CharField(blank=True, max_length=30)),
                ('telephone', models.CharField(blank=True, max_length=30)),
                ('credit_card', models.CharField(blank=True, max_length=30)),
                ('seat_preference', models.CharField(choices=[(None, 'Please select a seating preference.'), ('window', 'Window Seat'), ('isle', 'Isle Seat'), ('none', 'No Preference')], max_length=30)),
                ('meal_preference', models.CharField(choices=[(None, 'Please select a meal preference.'), ('veg', 'Vegitarian'), ('none', 'No Preference')], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
