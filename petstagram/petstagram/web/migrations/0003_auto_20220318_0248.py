# Generated by Django 3.1.1 on 2022-03-18 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20220317_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]