# Generated by Django 4.1.3 on 2022-11-20 19:48

import IT_TaskPortal.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_appuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), IT_TaskPortal.accounts.validators.validate_only_letters], verbose_name='Име/First_name'),
        ),
    ]
