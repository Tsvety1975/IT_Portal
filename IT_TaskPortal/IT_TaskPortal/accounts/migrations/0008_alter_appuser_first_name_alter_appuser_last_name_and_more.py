# Generated by Django 4.1.3 on 2022-11-23 14:28

import IT_TaskPortal.accounts.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_appuser_user_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), IT_TaskPortal.accounts.validators.validate_only_letters], verbose_name='Име | First name'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), IT_TaskPortal.accounts.validators.validate_only_letters], verbose_name='Фамилия | Family name'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[IT_TaskPortal.accounts.validators.validate_only_digits, django.core.validators.MinLengthValidator(9)], verbose_name='Мобилен/служебен номер | Mobile/work phone number'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='position',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Длъжност | Position'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='shor', to='accounts.department', verbose_name='Дирекция  | Department'),
        ),
    ]
