# Generated by Django 5.0.7 on 2024-08-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_customers_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$SFjubXozEwKNmQiMLCqWUE$xxEIKVy3x9TKGlzlsAbcuyZtfHbvn9bojsc5dNqbCb0=', max_length=128),
        ),
    ]
