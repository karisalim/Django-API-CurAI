# Generated by Django 5.1.6 on 2025-02-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0003_specialization_customuser_consultation_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='default_username', max_length=255, unique=True),
        ),
    ]
