# Generated by Django 4.1.3 on 2022-12-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
