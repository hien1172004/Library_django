# Generated by Django 5.1.2 on 2024-11-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_rename_student_id_librarylog_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
