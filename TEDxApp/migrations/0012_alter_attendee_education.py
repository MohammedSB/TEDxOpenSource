# Generated by Django 4.2 on 2023-04-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEDxApp', '0011_remove_attendee_city_attendee_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='education',
            field=models.CharField(choices=[('high_school', 'high_school'), ('university', 'university'), ('bachelors', 'bachelors'), ('masters', 'masters'), ('doctorate', 'doctorate')], max_length=50),
        ),
    ]