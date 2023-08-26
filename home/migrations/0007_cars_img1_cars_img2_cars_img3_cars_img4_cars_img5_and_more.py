# Generated by Django 4.2.3 on 2023-08-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_home_paragerafe_asli_alter_home_imgone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='img1',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AddField(
            model_name='cars',
            name='img2',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AddField(
            model_name='cars',
            name='img3',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AddField(
            model_name='cars',
            name='img4',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AddField(
            model_name='cars',
            name='img5',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AddField(
            model_name='cars',
            name='parag',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='parag1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='color',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='img',
            field=models.ImageField(upload_to='home/files/covers'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='kms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='maintance',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='imgone',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AlterField(
            model_name='home',
            name='imgthree',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AlterField(
            model_name='home',
            name='imgtwo',
            field=models.ImageField(blank=True, upload_to='home/files/covers'),
        ),
        migrations.AlterField(
            model_name='home',
            name='paragone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='paragthree',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='paragtwo',
            field=models.TextField(blank=True),
        ),
    ]
