# Generated by Django 4.0.6 on 2022-07-31 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('rules', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
