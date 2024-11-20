# Generated by Django 5.1.2 on 2024-11-20 18:29

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_librarylog_checked_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransaction',
            name='id',
            field=models.CharField(default=home.models.generate_trans, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=home.models.generate_category, editable=False, max_length=13, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='librarylog',
            name='checked_in',
            field=models.BigIntegerField(default=1732127385),
        ),
        migrations.AlterField(
            model_name='librarylog',
            name='id',
            field=models.CharField(default=home.models.generate_library, editable=False, max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
