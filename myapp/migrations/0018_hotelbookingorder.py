# Generated by Django 4.0.3 on 2023-11-05 07:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_hotelbookingmemberdetail_aadhaar_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBookingOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paid_amount', models.FloatField(default=0, null=True)),
                ('currency', models.CharField(choices=[('INR', 'Indian Rupees'), ('USD', 'US Dollar')], default='USD', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('hotel_booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='hotel_booking_orders', to='myapp.hotelbooking')),
            ],
        ),
    ]
