# Generated by Django 3.2.9 on 2021-12-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211208_0602'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.UniqueConstraint(fields=('subscribing', 'subscriber'), name='unique_subscribing_subscriber'),
        ),
    ]
