# Generated by Django 3.2.13 on 2022-05-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='introduce',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
