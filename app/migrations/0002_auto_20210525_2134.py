# Generated by Django 3.1.11 on 2021-05-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='introduction',
            field=models.TextField(verbose_name='自己紹介'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.TextField(verbose_name='仕事'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subimage',
            field=models.ImageField(upload_to='images', verbose_name='サブ画像'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='サブタイトル'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='topimage',
            field=models.ImageField(upload_to='images', verbose_name='トップ画像'),
        ),
    ]
