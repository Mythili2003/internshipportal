# Generated by Django 4.2.3 on 2023-07-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internportal', '0006_internship_details_perks_and_benefits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='jobtitle',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
