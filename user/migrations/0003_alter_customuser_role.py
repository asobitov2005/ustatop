# Generated by Django 5.0.6 on 2025-05-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_date_joined_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('client', 'client'), ('usta', 'usta'), ('admin', 'admin')], max_length=20),
        ),
    ]
