# Generated by Django 3.2.20 on 2023-09-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]