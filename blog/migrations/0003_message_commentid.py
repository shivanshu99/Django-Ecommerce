# Generated by Django 2.2.10 on 2020-06-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_message_commentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='commentId',
            field=models.IntegerField(default=0),
        ),
    ]
