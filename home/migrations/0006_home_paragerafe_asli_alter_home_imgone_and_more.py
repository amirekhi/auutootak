# Generated by Django 4.2.3 on 2023-08-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_img1_home_imgone_rename_img2_home_imgthree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='paragerafe_asli',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='imgone',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='home',
            name='imgthree',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='home',
            name='imgtwo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
