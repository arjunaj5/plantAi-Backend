# Generated by Django 4.0.1 on 2022-02-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='comments',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
