from django.db import models
from django.urls import reverse


class People(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')  # Заголовок или имя (макс. 255 символов)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") # # Поле для хранения уникального URL-адреса (слага), индексируемое для быстрого поиска.
    content = models.TextField(blank=True, verbose_name='Контент')  # Текстовое поле, может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')  # Путь для загрузки фото
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')  # Время создания записи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')  # Время обновления записи
    is_published = models.BooleanField(default=True, verbose_name='Публикация')  # Статус публикации (по умолчанию — опубликовано)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')  # Связь с таблицей категорий


    def __str__(self):
        return self.title  # Возвращает название записи


    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "знаменитость"
        verbose_name_plural = 'Знаменитости'
        ordering = ['time_create', 'title']
        
        
        
class Category(models.Model):
    name = models.CharField( # Название категории
        
        max_length=100, # Максимальная длина строки
        db_index=True,  # Добавить индекс в базе данных
        verbose_name='Категория', # Читаемое название поля
    )

    slug = models.SlugField(  
        max_length=255,  # Максимальная длина строки
        unique=True,     # Значение должно быть уникальным
        db_index=True,   # Добавить индекс в базе данных
        verbose_name="URL"  # Читаемое название поля
    )
      
      
    def __str__(self):
        return self.name  # Для отображения названия категории в админке
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = 'категорию' # Название модели в единственном числе.
        verbose_name_plural = 'Категории' # Название модели во множественном числе.
        ordering = ['id'] # Сортировка записей по ID.
    
    
    
    