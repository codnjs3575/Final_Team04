# Generated by Django 3.2.13 on 2022-05-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20220504_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='service',
            field=models.IntegerField(choices=[(1, '★'), (2, '★'), (3, '★'), (4, '★'), (5, '★')], default=3),
            preserve_default=False,
        ),
    ]