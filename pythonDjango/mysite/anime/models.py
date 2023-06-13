from django.db import models
from django.urls import reverse

class Gener(models.Model):
    """ Жанры """
    name = models.CharField('Название жанра:', max_length=50)
    description = models.TextField('Описание:', blank=True)
    url = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Direction(models.Model):
    """Режиссеры"""
    name = models.CharField('Фамилия и Имя:', max_length=150)
    description = models.TextField('Биография:', blank=True)
    image = models.ImageField('Фотография', upload_to='image/direction/%Y')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Anime(models.Model):
    """Информация о Аниме """
    titel = models.CharField('Название аниме:', max_length=100)
    imag = models.ImageField('Постер', upload_to='image/%Y')
    description = models.TextField('Описание:', blank=True)
    date_pupl = models.DateTimeField("Дата выхода:")
    directions = models.ManyToManyField(Direction, verbose_name='Режиссер')
    gener = models.ManyToManyField(Gener, verbose_name='Жанр')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.titel}, {self.date_pupl }'


    def get_absolute_url(self):
        return reverse('anime_detel', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length= 50)
    text_reviews = models.TextField('Текст озыва', max_length= 500)
    anime = models.ForeignKey(Anime, verbose_name='Аниме', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.anime }'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'