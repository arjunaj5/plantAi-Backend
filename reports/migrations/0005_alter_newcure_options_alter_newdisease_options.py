# Generated by Django 4.0.1 on 2022-03-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_rename_iscorrection_newdisease_is_correction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newcure',
            options={'verbose_name_plural': 'NewCure'},
        ),
        migrations.AlterModelOptions(
            name='newdisease',
            options={'verbose_name_plural': 'NewDiseases'},
        ),
    ]