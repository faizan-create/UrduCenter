# Generated by Django 3.1.5 on 2021-02-17 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urduweb', '0033_auto_20210216_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='urduweb.category'),
        ),
    ]
