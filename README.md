# covidapi
# install django

pip install django

# install rest_framework

pip install rest_framework

# create project

django-admin startproject projectname

# open setting.py file of your project 

DATABASES = {

    'default': {

'ENGINE': 'djongo',

'NAME': 'your-db-name',

    }
}

in installed app 

mention there appname,

and rest_framework

# run
manage.py makemigrations

manage.py migrate

# create app

python3 manage.py startapp appname

# run on server

python3 manage.py runserver

