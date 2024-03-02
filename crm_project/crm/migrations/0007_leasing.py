# Generated by Django 5.0.1 on 2024-01-24 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leasing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lease_start_date', models.DateField()),
                ('lease_end_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.cars')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
            ],
        ),
    ]