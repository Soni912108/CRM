# Generated by Django 5.0.1 on 2024-01-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_remove_transaction_car_feature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='number_of_cars_in_lease',
            field=models.IntegerField(null=True),
        ),
    ]