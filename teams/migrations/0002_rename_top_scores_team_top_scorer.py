# Generated by Django 5.1.4 on 2024-12-17 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='top_scores',
            new_name='top_scorer',
        ),
    ]
