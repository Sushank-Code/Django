# Generated by Django 5.1.7 on 2025-04-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
