# Generated by Django 3.2.6 on 2021-08-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('html_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
