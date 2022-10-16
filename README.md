# Запуск проекта
* Клонируем [репозиторий](https://github.com/Sus-arch/DjangoYandex)

  ```
  git clone https://github.com/Sus-arch/DjangoYandex.git
  ```
  
* Переходим в репозиторий 
 
  ```
  cd DjangoProject  
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
  
  * Запускаем сайт 
  
  ```
  python3 manage.py runserver 8080
  ```
  
* Переходим по ссылке http://localhost:8080/
