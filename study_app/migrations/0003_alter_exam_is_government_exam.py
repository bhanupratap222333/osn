# Generated by Django 5.0.4 on 2024-09-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_app', '0002_alter_user_address_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='is_government_exam',
            field=models.BooleanField(default=True),
        ),
    ]
