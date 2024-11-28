# Generated by Django 5.0.7 on 2024-08-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0002_alter_purchaseorder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
