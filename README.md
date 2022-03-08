# Common-use commands

## Run Server

```bash
python manage.py runserver
```

## Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

## Create an App

```bash
python manage.py startapp nombreApp
```

----

## To create a working app

1. Create the app and **add its path to the general [*urls.py*](./djangoproject/urls.py) file.** *REMEMBER!* Add it to both **the import & the urlpattern**
2. Add the **app name** to the [*djangoproject/settings.py* file](./djangoproject/settings.py) inside the **INSTALLED_APPS** variable (after the comment in line 37, #Django Project Apps)
3. Copy the [*urls.py*](./exampleApp/urls.py) of the example app into your new one and **change the *app_name* variable** that is written after the imports
4. Copy the [*models.py*](./exampleApp/models.py) and [*forms.py*](./exampleApp/forms.py) of the **exampleApp** and adequate their logic to fit your new app.
5. You'll most probably need to change the [*views.py*](./exampleApp/views.py) logic
6. Finally, change all of the urls from exampleApp (**eg. *exampleApp:index***) for the **app name** that you set.

----

## Create your Virtual Env and install requirements

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Create a superuser for the Django admin

```bash
python manage.py createsuperuser
```

Remember that you have to add your current model into the app's admin.py in order for it to list the entity in the Django Admin


## Create a requirements.txt file

```bash
pip freeze > requirements.txt
```

----

## To preview this markdown file in VSCode

1. Download the Markdown Preview Github Extension
2. Hit **Ctrl + Shift + V**
