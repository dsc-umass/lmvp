# Generated by Django 3.0.6 on 2020-06-21 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmvpinterface', '0006_auto_20200621_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Metric',
            new_name='NumericMetric',
        ),
        migrations.RenameModel(
            old_name='Property',
            new_name='TextMetric',
        ),
    ]
