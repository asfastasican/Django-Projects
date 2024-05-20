# Generated by Django 5.0.1 on 2024-04-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
