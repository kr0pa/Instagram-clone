# Generated by Django 5.0.6 on 2024-05-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_post', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
