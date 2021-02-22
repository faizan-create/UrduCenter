# Generated by Django 3.1.4 on 2021-02-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urduweb', '0006_recentpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuasPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PeotyPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
