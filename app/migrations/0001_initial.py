# Generated by Django 3.1.11 on 2021-05-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('job', models.TextField(verbose_name='shigoto')),
                ('introduction', models.TextField(verbose_name='jikoshokai')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='linkedin')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='facebook')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram')),
                ('topimage', models.ImageField(upload_to='images', verbose_name='top image')),
                ('subimage', models.ImageField(upload_to='images', verbose_name='sub image')),
            ],
        ),
    ]
