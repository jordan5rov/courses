# Generated by Django 4.0.2 on 2022-02-11 18:51

from django.db import migrations, models
import petstagram.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_petphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='', validators=[petstagram.web.validators.validate_file_max_size_in_mb]),
        ),
    ]