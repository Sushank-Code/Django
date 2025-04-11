# Generated by Django 5.1.7 on 2025-04-11 14:19

import model_serializer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_serializer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=20, unique=True, validators=[model_serializer.models.strict_email_validator]),
        ),
    ]
