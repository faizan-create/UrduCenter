# Generated by Django 3.1.4 on 2021-02-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urduweb', '0004_auto_20210205_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]