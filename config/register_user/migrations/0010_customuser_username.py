# Generated by Django 5.1.6 on 2025-02-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0009_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
