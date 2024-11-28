# Generated by Django 5.0.7 on 2024-08-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customers_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customers',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$9vLopN7jd3m6vpDTQ4rfap$KiWCW2giTmJ0WHfv75ueaMAEGMYUed5glYdgditkQAY=', max_length=128),
        ),
    ]
