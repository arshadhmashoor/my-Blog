# Generated by Django 4.0.2 on 2022-02-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='this is default blog', max_length=255),
        ),
    ]
