# Generated by Django 4.1.4 on 2023-03-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0006_remove_posts_comment_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
