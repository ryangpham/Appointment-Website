# Generated by Django 5.0.7 on 2024-08-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_appointment_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]