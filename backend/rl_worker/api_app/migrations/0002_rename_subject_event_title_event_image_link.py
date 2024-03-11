# Generated by Django 5.0.1 on 2024-03-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='subject',
            new_name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='image_link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]