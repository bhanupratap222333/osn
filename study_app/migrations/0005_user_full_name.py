# Generated by Django 5.0.4 on 2024-10-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_app', '0004_alter_exam_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='user_name', max_length=50),
        ),
    ]