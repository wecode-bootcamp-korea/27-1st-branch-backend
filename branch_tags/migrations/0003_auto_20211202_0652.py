# Generated by Django 3.2.9 on 2021-12-02 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch_tags', '0002_auto_20211202_0625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postingtag',
            old_name='posting',
            new_name='postings',
        ),
        migrations.RenameField(
            model_name='usertag',
            old_name='user',
            new_name='users',
        ),
    ]