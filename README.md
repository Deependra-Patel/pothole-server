# Pothole Reporting Android app's server implementation in Django

## Installation
1. Install postgresql ("sudo apt-get install postgresql postgresql-contrib")
2. Install postgis ("sudo apt-get install postgresql-9.5-postgis-2.1")
3. Create user 'potholeuser' with password 'mypass' in psql, create database 'potholedb' with postgis extension in it, grant superuser permission to 'potholeuser'
   1. "sudo -i -u postgres"
   2. "create user potholeuser with password 'mypass'"
   3. "psql"
   4. "create database potholedb;"
   5. "\c potholedb;"
   6. "create extension postgis;"
   7. "grant all privileges on database potholedb to potholeuser;"
   8. "alter user potholeuser with superuser;"
4. Install libpq-dev and python dev ("sudo apt-get install libpq-dev python-dev")
5. Install pip
6. Install virtualenv ("pip install virtualenv")
7. Create the virtual environment and activate it
8. Install requirements using pip ("pip install -r requirements.txt")
If Pillow doesn't build then, "sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk"
9. (local) Use pip to install "isort", "pep8" and "pylint" for development
10. (optional) Install spatialite for quickly running automated tests while writing tests(Will also have to update settings) ("sudo apt-get install libsqlite3-mod-spatialite")
11. Run tests in directory ("coverage run --source '.' manage.py test")
12. Create super user ("python manage.py createsuperuser")
13. Run server ("python manage.py runserver")
