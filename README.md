# Запуск проекта
* Клонируем [репозиторий](https://github.com/Sus-arch/DjangoWeb)

  ```
  git clone https://github.com/Sus-arch/DjangoWeb.git
  ```
  
* Переходим в репозиторий 
 
  ```
  cd DjangoWeb
  ```
  
* Активируем виртуальное окружение
  ##### Для Windows
  ```
  python -m venv venv
  ```
  ```
  venv/Scripts/activate
  ```
  * Устанавливаем зависимости

  ```
  pip install -r requirements.txt
  ```
  
  * Редактирование переменный среды

    - Открыть файл .env.example
    - Изменить значение SECRET_KEY на свой ключ

  * Запускаем сайт 
  
  ```
  python manage.py runserver 8080
  ```
  ##### Для Linux и MacOS
  ```
  python3 -m venv venv
  ```
  ```
  source venv/bin/activate
  ```
  * Устанавливаем зависимости

  ```
  pip3 install -r requirements.txt
  ```
  
  * Редактирование переменный среды

    - Открыть файл .env.example
    - Изменить значение SECRET_KEY на свой ключ
  
  * Запускаем сайт 
  
  ```
  python3 manage.py runserver 8080
  ```

* Переходим по ссылке http://localhost:8080/
# База данных
* [ER-диаграмма БД](https://app.quickdatabasediagrams.com/#/d/aXJwXG) 
