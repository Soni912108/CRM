# Generated by Django 5.0.1 on 2024-01-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leasing',
            name='amount',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
    ]
