# Generated by Django 4.1.7 on 2023-03-22 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_anime_date_pupl_alter_anime_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='emeil',
            new_name='email',
        ),
    ]
