# Generated by Django 5.1.1 on 2024-09-15 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offences',
            name='penal_code',
            field=models.CharField(max_length=10),
        ),
    ]
