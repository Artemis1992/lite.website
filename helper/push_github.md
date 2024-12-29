git remote add origin https://github.com/Artemis1992/lite.website.git
git branch -M main
git push -u origin main

***
### Создание файла:
```git add .gitignore```


### Эта команда создаст файл .gitignore и добавит в него строку, исключающую папку venv (Если ее небыло у нас).
```echo venv/ > .gitignore ```
***
***
## Удаляем папку venv из репозитория github
**Если вы ещё не удалили папку venv из локального репозитория, выполните команду:**
```
git rm -r --cached venv
```
**Затем добавьте её в .gitignore (если этого ещё не сделано):**
```
echo "venv/" >> .gitignore
git add .gitignore
git commit -m "Удалена папка venv из репозитория и добавлена в .gitignore"
```
### Отправьте изменения в удалённый репозиторий
После удаления папки venv из индекса локального репозитория отправьте изменения на GitHub:
```
git push
```
***
***