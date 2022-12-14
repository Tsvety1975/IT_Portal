# Generated by Django 4.1.3 on 2022-12-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_alter_taskfornewworker_access_to_read_write_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfornewworker',
            name='status',
            field=models.CharField(choices=[('open', 'Нов'), ('in_progress', 'В прогрес'), ('pending', 'Очаква изпълнение'), ('partial_executed', 'Частично изпълненa'), ('close', 'Приключена')], default='Очаква изпълнение', max_length=50, verbose_name='Статус| State'),
        ),
    ]
