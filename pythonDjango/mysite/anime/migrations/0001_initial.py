# Generated by Django 4.1.7 on 2023-03-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Фамилия и Имя')),
                ('description', models.TextField(blank=True, verbose_name='Биография')),
                ('image', models.ImageField(upload_to='image/direction/%Y', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Gener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название жанра')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('url', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100, verbose_name='Название аниме')),
                ('imag', models.ImageField(upload_to='image/%Y', verbose_name='Постер')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('date_pupl', models.DateTimeField(verbose_name='Дата выхода')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('directions', models.ManyToManyField(to='anime.direction', verbose_name='Открыватель')),
                ('gener', models.ManyToManyField(to='anime.gener', verbose_name='Вид')),
            ],
            options={
                'verbose_name': 'Аниме',
                'verbose_name_plural': 'Аниме',
            },
        ),
    ]