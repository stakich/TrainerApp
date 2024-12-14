# Generated by Django 5.1.1 on 2024-12-11 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_first_name_alter_appuser_last_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_approved',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='specialization',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]