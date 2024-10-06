"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.conf.urls.static import static
from coolsite import settings
from django.contrib import admin
from django.urls import path
from people.views import pageNotFound

 # это все функции которые обрабатывают запросы.
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Эта строка включает URL-маршруты из файла `people.urls` в основной конфигурации URL-адресов приложения.
    # Когда пользователь обращается к адресу, начинающемуся с `people/`, Django ищет соответствующий маршрут
    # в файле `people/urls.py`. Таким образом, маршруты в `people.urls` становятся частью общей структуры
    # URL-адресов проекта.
    path('', include('people.urls'))
    # Если захотим добавить еще приложение по мимо people то, мы тут пропишем к нему маршрут, точно так же как и people
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound


