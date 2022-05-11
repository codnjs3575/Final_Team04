# Generated by Django 3.2.13 on 2022-05-02 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
        ('member', '0002_alter_user_managers_user_birth_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='likelike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'likelike',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='like_reviews',
            field=models.ManyToManyField(blank=True, related_name='like_users', through='member.likelike', to='review.Review'),
        ),
    ]