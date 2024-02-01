# Generated by Django 4.2.9 on 2024-01-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('start_date', models.DateField()),
                ('position', models.CharField()),
                ('salary', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=10)),
            ],
        ),
    ]
