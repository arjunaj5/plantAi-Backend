# Generated by Django 4.0.1 on 2022-02-20 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diseases', '0007_detectionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diseases.detectionhistory')),
            ],
            options={
                'verbose_name_plural': 'Report',
            },
        ),
    ]
