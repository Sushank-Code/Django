# Generated by Django 5.1.7 on 2025-03-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_authapp', '0002_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
