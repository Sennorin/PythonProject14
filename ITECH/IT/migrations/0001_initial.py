# Generated by Django 5.1.6 on 2025-02-26 23:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Introduction', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('business_Hours', models.CharField(max_length=100)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('main_image', models.ImageField(upload_to='main_images/', verbose_name='main_picture')),
                ('restaurant_image', models.ImageField(upload_to='restaurant_images/', verbose_name='restaurant_picture')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
