# Generated by Django 4.0.1 on 2022-02-22 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_newdisease_newcure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newdisease',
            old_name='isCorrection',
            new_name='is_correction',
        ),
    ]
