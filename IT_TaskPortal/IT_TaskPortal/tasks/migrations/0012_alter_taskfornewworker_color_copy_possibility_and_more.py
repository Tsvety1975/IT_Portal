# Generated by Django 4.1.3 on 2022-12-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_taskfornewworker_rights_same_as_worker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfornewworker',
            name='color_copy_possibility',
            field=models.BooleanField(null=True, verbose_name='Цветно копиране| Color copy'),
        ),
        migrations.AlterField(
            model_name='taskfornewworker',
            name='monitor',
            field=models.BooleanField(null=True, verbose_name='Монитор | Monitor'),
        ),
        migrations.AlterField(
            model_name='taskfornewworker',
            name='scaner',
            field=models.BooleanField(null=True, verbose_name='Скенер| Scanner'),
        ),
    ]
