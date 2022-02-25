# Generated by Django 4.0.2 on 2022-02-24 00:02

import django.core.validators
from django.db import migrations, models
import expenses_tracker_exam_prep.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses_tracker_exam_prep.web.validators.only_letters_validator]),
        ),
    ]
