# Generated by Django 4.0.2 on 2022-02-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click abov link to read blog..', max_length=255),
        ),
    ]
