```
pip install django
django-admin startproject mysite
cd mysite 
python manage.py migrate

# Когда нужно запускать приложение в разных окружениях
python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings

python manage.py startapp blog
```

```
 python manage.py shell
 from blog.models import Post
 Post.Status.choices
 Post.Status.labels
 Post.Status.values
 Post.Status.names
```

```
python manage.py makemigrations blog
python manage.py sqlmigrate blog 0001

python manage.py createsuperuser
python manage.py runserver
```