# Generated by Django 3.1.6 on 2021-02-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='online_pay',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='spec',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='week_days',
            field=models.TextField(default='[false,false,false,false,false,false,false]', max_length=1000),
        ),
    ]
