# Generated by Django 3.1.5 on 2021-02-06 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urduweb', '0017_remove_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='start_date',
        ),
    ]
