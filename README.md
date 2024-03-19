### UZ

*Dasturni ishlatish uchun quyidagi qadamlarni bajaring:*

1. ```git clone https://github.com/JahongirHakimjonov/FelixCompanyTask.git```
2. ```cd FelixCompanyTask```
3. ```python -m venv venv```
4. ```source venv/bin/activate``` (Linux) yoki ```venv\Scripts\activate``` (Windows)
5. ```pip install -r requirements.txt```
6. ```python manage.py makemigrations```
7. ```python manage.py migrate```
8. ```python manage.py createsuperuser```
9. ```python manage.py runserver```

*Barcha qadamlar to'g'ri bajarilgach, dastur ishga tushadi.*
Dastur ish tushgandan so'ng, brauzeringizda ```http://127.0.0.1:8000/api/v1/``` manziliga kirib, API-ni test qilishingiz mumkin.

*Ushbu dasturda quyidagi funksiyalar mavjud:*

1. ```/admin``` - Admin panel
2. ```/api/v1``` - API routerlar

### !!!Diqqat!!! Dastur ishga tushirishdan oldin, .env nomli file yarating va unga .env_file.txt faylidagi malumotlarni kiritib qo'ying va
```python manage.py runserver``` 
komandasini bajaring.


### Eslatma: Daastur PostgresSQL dan foydalangan holda yaratilgan. Agar sizda PostgresSQL o'rnatilmagan bo'lsa, dasturni ishga tushirishda xatolik yuzaga kelishi mumkin. Buning uchun, dasturda foydalanilgan bazani SQLite ga o'zgartirish kerak yoki "products" nomli baza yaratish kerak va .env file dagi SQL_PASSWORD nomli qatorga o'zingizga tegishli parolni yozishingiz kerak.

### RU 

*Чтобы использовать программу, выполните следующие шаги:*

1. ```git clone https://github.com/JahongirHakimjonov/FelixCompanyTask.git```
2. ```cd FelixCompanyTask```
3. ```python -m venv venv```
4. ```source venv/bin/activate``` (Linux) или ```venv\Scripts\activate``` (Windows)
5. ```pip install -r requirements.txt```
6. ```python manage.py makemigrations```
7. ```python manage.py migrate```
8. ```python manage.py createsuperuser```
9. ```python manage.py runserver```

*После выполнения всех шагов программа запустится.*
После запуска программы вы можете протестировать API, перейдя по адресу ```http://127.0.0.1:8000/api/v1/``` в вашем браузере. 

*В этой программе доступны следующие функции:*

1. ```/admin``` - Админ панель
2. ```/api/v1``` - API роутеры

### !!!Внимание!!! Перед запуском программы создайте файл с именем .env и вставьте в него данные из файла .env_file.txt, а затем выполните команду
```python manage.py runserver```

### Внимание: Программа создана с использованием PostgresSQL. Если у вас не установлен PostgresSQL, то при запуске программы может возникнуть ошибка. Для исправления этой ошибки вам нужно изменить базу данных на SQLite или создать базу данных с именем "products" и в .env файле в строке SQL_PASSWORD вставить свой пароль.
