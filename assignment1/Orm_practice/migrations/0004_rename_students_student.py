# Generated by Django 4.1.5 on 2023-02-03 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orm_practice', '0003_students_school_student_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]