# Generated by Django 4.2.3 on 2023-07-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Internship_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('duration', models.CharField(max_length=50)),
                ('vacancies', models.PositiveIntegerField()),
                ('last_date_to_apply', models.DateField()),
                ('internship_type', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
            ],
        ),
    ]
