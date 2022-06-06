# simple_blog_with_django

[Link to Youtube course](https://youtu.be/B40bteAMM_M)

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject django_blog .  
3. Generate application : python3 manage.py startapp blog 


# To migrate 
1. python manage.py makemigrations
2. python manage.py migrate

# For admin
- Create super user : python3 manage.py createsuperuser

# Run server
python3 manage.py runserver 127.0.0.1:8002



