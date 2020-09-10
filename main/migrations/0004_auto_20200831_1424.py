# Generated by Django 3.1 on 2020-08-31 08:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200831_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='grading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5)),
                ('interest', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='suggestCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='takenCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='semester',
        ),
        migrations.AlterField(
            model_name='interest',
            name='interest',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='grading',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.takencourses'),
        ),
    ]
