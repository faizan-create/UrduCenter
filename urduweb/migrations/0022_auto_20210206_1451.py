# Generated by Django 3.1.5 on 2021-02-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urduweb', '0021_auto_20210206_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentpost',
            name='pub_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]