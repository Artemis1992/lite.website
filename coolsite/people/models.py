from django.db import models
from django.urls import reverse

class People(models.Model):
    title = models.CharField(max_length=255)  # Заголовок или имя (макс. 255 символов)
    content = models.TextField(blank=True)  # Текстовое поле, может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")  # Путь для загрузки фото
    time_create = models.DateTimeField(auto_now_add=True)  # Время создания записи
    time_update = models.DateTimeField(auto_now=True)  # Время обновления записи
    is_published = models.BooleanField(default=True)  # Статус публикации (по умолчанию — опубликовано)

    def __str__(self):
        return self.title  # Возвращает название записи


    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
    