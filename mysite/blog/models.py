from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class PublishedManager(models.Manager):
    """
    Пример создания модельного мменеджера
    """
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    objects = models.Manager()      # менеджер по умолчанию
    published = PublishedManager()  # Конкретно прикладной менеджер

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    # Не может быть два одинаковых слага с одной датой публикации
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    body = models.TextField()

    # timezone.now - вернет дату и время в формате зависящем от часового пояса
    publish = models.DateTimeField(default=timezone.now)
    # Дата и время создания поста
    created = models.DateTimeField(auto_now_add=True)
    # последняя дата обновления поста
    # auto_now - обновляет дату и время автоматически
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        # Сортируем в обратном порядке
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        :return:  Канонический адрес объекта
        """
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

