
### В Django GET и POST-запросы обрабатываются с помощью представлений (views) и форм. Рассмотрим их работу на примерах.

# 1. GET-запрос в Django

**GET-запрос используется для получения данных, например, для отображения страницы с формой или списка объектов.**

**Пример GET-запроса (вывод списка пользователей)**

```
from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()  # Получаем всех пользователей из базы
    return render(request, 'users.html', {'users': users})
```

**🔹 Здесь ```request``` — объект запроса, который содержит все данные о GET-запросе.**

**🔹 ```User.objects.all()``` — получаем список пользователей из базы.**

**🔹 ```render()``` отправляет данные в шаблон ```users.html```.**

### Шаблон (```users.html```):

```
<!DOCTYPE html>
<html>
<head><title>Список пользователей</title></head>
<body>
    <h2>Пользователи</h2>
    <ul>
        {% for user in users %}
            <li>{{ user.username }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```
**Как это работает?**
**Если пользователь открывает страницу ```/users/```, сервер делает GET-запрос, получает список пользователей и рендерит их в HTML.**


***
# 2. POST-запрос в Django

**POST-запрос используется для отправки данных, например, для обработки формы регистрации или входа в систему.**

### Пример POST-запроса (форма входа)


**Форма отправляет данные методом POST, и сервер обрабатывает их.**

```
from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Получаем данные из формы
        password = request.POST.get('password')
        
        # Проверяем логин и пароль (упрощенная версия, без БД)
        if username == 'admin' and password == '123':
            return HttpResponse(f'Добро пожаловать, {username}!')
        else:
            return HttpResponse('Неверный логин или пароль')
    
    return render(request, 'login.html')  # Показываем форму, если GET-запрос
```
**Шаблон (```login.html```):**

```
<!DOCTYPE html>
<html>
<head><title>Авторизация</title></head>
<body>
    <h2>Вход</h2>
    <form method="post">
        {% csrf_token %}  <!-- Защита Django от атак CSRF -->
        <label>Логин:</label>
        <input type="text" name="username"><br>
        <label>Пароль:</label>
        <input type="password" name="password"><br>
        <button type="submit">Войти</button>
    </form>
</body>
</html>
```
**🔹 Если запрос GET, просто отображаем форму.**

**🔹 Если POST, берём ```username``` и ```password``` из ```request.POST```, проверяем их и выдаём результат.**

**🔹 ```{% csrf_token %}``` — обязательный токен, который защищает форму от атак CSRF.**
***

# 3. Комбинированный GET и POST (форма регистрации)

**Можно обрабатывать и GET, и POST в одном представлении.**

```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Создаём пользователя (в реальном проекте нужен хеш пароля)
        User.objects.create(username=username, password=password)
        return HttpResponse('Регистрация успешна!')

    return render(request, 'register.html')  # Если GET-запрос, показываем форму
```
🔹 User.objects.create(username=username, password=password) — создаёт нового пользователя в БД.

🔹 Если регистрация успешна, отправляем сообщение Регистрация успешна!.

🔹 Если GET-запрос, просто показываем пустую форму.
***

# 4. GET с параметрами (поиск)
**Django позволяет получать параметры через ```request.GET```.**

**Пример: поиск пользователей по имени.**
```
def search_user(request):
    query = request.GET.get('q')  # Получаем параметр q из URL

    if query:
        users = User.objects.filter(username__icontains=query)  # Фильтруем по имени
    else:
        users = User.objects.all()  # Если нет запроса, показываем всех

    return render(request, 'search.html', {'users': users})
```

**Теперь если открыть в браузере ```http://127.0.0.1:8000/search?q=admin```, Django отфильтрует пользователей по имени ```admin```.**

**Шаблон (```search.html```):**
```
<form method="get">
    <input type="text" name="q" placeholder="Введите имя">
    <button type="submit">Искать</button>
</form>

<ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor %}
</ul>
```

**🔹 request.GET.get('q') получает параметр из URL**.

**🔹 Если параметр есть, ищем пользователей по username__icontains=query.**
***

## **Вывод**

| Запрос | Когда используется? | Как передаются данные? | Где их брать в Django? |
|--------|---------------------|------------------------|------------------------|
| **GET** | Получение данных, отображение страниц | В URL (например, `?q=python`) | `request.GET.get('param')` |
| **POST** | Отправка форм, регистрация, вход | В теле запроса (скрыто) | `request.POST.get('param')` |

**Если передаёшь конфиденциальные данные (пароли, формы) → POST.**

**Если просто отображаешь информацию или ищешь → GET.**


