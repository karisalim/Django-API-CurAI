# Generated by Django 5.1.6 on 2025-02-25 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorreview',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
