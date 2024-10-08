# Generated by Django 5.1 on 2024-08-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=10)),
                ('director', models.CharField(max_length=255)),
                ('poster_url', models.URLField()),
                ('synopsis', models.TextField()),
                ('rotten_tomatoes', models.CharField(default='N/A', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
