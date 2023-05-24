# Generated by Django 3.1.14 on 2023-05-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0003_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='deliver',
            field=models.BooleanField(default=False, null=True, verbose_name='Услуга оказана'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='tentatively',
            field=models.BooleanField(default=True, null=True, verbose_name='Предварительная запись'),
        ),
    ]