# summary (steve.no)

## create venv 
```
python -m venv venv
pip install django
pip install psycopg2
pip install --upgrade pip
where python
```

## create django project 
chose core or startproject
```
python -m django --version
django-admin startproject mysite
python ./mysite/manage.py runserver 0:8000
```

## create and run docker-compose
- see how to configure network to couple pgadmin and postgres
- see how to link volumes to container 
```
pip freeze > requirements.txt
docker-compose up
docker inspect xyz
```

## migrate data
this super user is user in django app 
```
python manage.py migrate
python manage.py createsuperuser 
```