# Generated by Django 4.1.4 on 2023-03-08 17:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialweb', '0007_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='comments',
            name='upvote',
            field=models.ManyToManyField(related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]