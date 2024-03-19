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

