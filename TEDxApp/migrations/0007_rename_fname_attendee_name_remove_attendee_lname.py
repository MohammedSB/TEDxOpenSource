# Generated by Django 4.0.3 on 2023-03-09 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TEDxApp', '0006_remove_seat_id_seat_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='lname',
        ),
    ]