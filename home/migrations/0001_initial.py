# Generated by Django 4.2.3 on 2023-08-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('cars_name', models.CharField(max_length=64)),
                ('kms', models.IntegerField()),
                ('color', models.TextField(max_length=64)),
                ('maintance', models.TextField(max_length=64)),
            ],
        ),
    ]
