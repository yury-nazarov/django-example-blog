from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    slug = models.SlugField(max_length=250)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    body = models.TextField()

    # timezone.now - вернет дату и время в формате зависящем от часового пояса
    publish = models.DateTimeField(default=timezone.now)
    # ДАта и время создания поста
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

