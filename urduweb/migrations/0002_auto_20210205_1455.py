# Generated by Django 3.1.4 on 2021-02-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urduweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('descrirption', models.TextField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='article',
        ),
    ]
