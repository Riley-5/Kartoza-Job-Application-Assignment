# Generated by Django 4.1 on 2022-08-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
