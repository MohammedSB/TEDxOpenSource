# Generated by Django 4.0.3 on 2023-04-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEDxApp', '0008_attendee_age_attendee_city_attendee_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='city',
            field=models.CharField(choices=[('riyadh', 'riyadh'), ('dammam', 'dammam'), ('jeddah', 'jeddah'), ('other', 'other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='confirmed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='education',
            field=models.CharField(choices=[('high_school', 'high_school'), ('university', 'university'), ('employed', 'employed')], max_length=50),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
