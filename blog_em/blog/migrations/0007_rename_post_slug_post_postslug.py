# Generated by Django 4.0.6 on 2022-08-10 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_space_slug_post_spaceslug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_slug',
            new_name='postslug',
        ),
    ]
