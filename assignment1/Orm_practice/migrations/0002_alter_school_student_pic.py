# Generated by Django 4.1.5 on 2023-02-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orm_practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='student_pic',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]
