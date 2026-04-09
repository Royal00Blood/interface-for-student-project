# interface-for-student-project

Это шаблон для создания веб интерфейса для проектной отчетности.

Для создания копии на своем рабочем ПК в терминале используйте команду:
```git clone https://github.com/Royal00Blood/interface-for-student-project.git```


## Для экспорта всех установленных библиотек проекта используйте:
### Для терминала:
```pip freeze > requirements.txt```
### Для окружения conda: 
```conda list --export > requirements.txt```

__Эта команда создаст файл со всеми библиотеками и их версиями автоматически.__

## Для установки из файла всех библиотек:
### Установить все библиотеки из requirements.txt:
```pip install -r requirements.txt```
### С повышенными правами (если нужно):
```sudo pip install -r requirements.txt```
### Для пользователя (без sudo):
```pip install --user -r requirements.txt```
