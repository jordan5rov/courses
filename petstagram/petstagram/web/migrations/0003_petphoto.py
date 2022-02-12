# Generated by Django 4.0.2 on 2022-02-11 18:51

from django.db import migrations, models
import petstagram.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.web.validators.validate_only_letters])),
                ('description', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='web.Pet')),
            ],
        ),
    ]