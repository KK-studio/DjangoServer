# Generated by Django 3.1.6 on 2021-02-07 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('phone', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('spec', models.IntegerField()),
                ('number', models.CharField(max_length=200)),
                ('online_pay', models.BooleanField()),
                ('experience_years', models.IntegerField(default=0)),
                ('address', models.CharField(default='none', max_length=1000)),
                ('week_days', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
