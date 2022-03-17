# Generated by Django 3.1.1 on 2022-03-17 00:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='user_profile',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Other', 'Other')], max_length=6),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user', 'name')},
        ),
    ]