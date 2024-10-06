from django.db import models

class People(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True) # Время создания, только при создании
    time_update = models.DateTimeField(auto_now=True) # Время обновления, при каждом изменении
    is_published = models.BooleanField(default=True)




