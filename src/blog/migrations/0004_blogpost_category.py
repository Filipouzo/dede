# Generated by Django 4.2 on 2023-05-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]