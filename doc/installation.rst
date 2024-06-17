.. _Installation:

============
Installation
============


From a Gitlab repository
======================

**Type this command on your terminal to clone the project:**

.. code-block::

    git clone 'https://gitlab.com/sf5810217/oc_lettings.git'


**Next, we need to create our local environment:**

.. code-block::

    python -m venv venv

**Now activate our local environment:**

*In Windows:*

.. code-block::

    venv/Scripts/activate.bat

*In MacOS:*

.. code-block::

    venv/bin/activate

**First, make an update of pip:**

.. code-block::

    python -m pip install --upgrade pip

**Second, we need to install all dependances:**

.. code-block::

    pip install -r requirements.txt

Environments variables
======================

**Finally, we must to create a .env files to add the environments variables:
Create a '.env' files and copy paste this code:**

.. code-block::

    SECRET_KEY="yoursecretkey"
    DSN="your dsn sentry"
    DJANGO_DEBUG='True'
    ALLOWED_HOSTS=['*']

**The secret key is a component essential for the security of your django application. She's use by Django
for:**

* cryptographic signatures
* password hashing
* injection protection

**The Sentry DSN is an url to allows the application to send events to your Sentry instance:**

* error
* exceptions
* messages

Build a Docker image to run the app locally
===========================================

**Download and install Docker**

Change to the project directory cd /path/to/OC_LETTINGS

1. Make sure that the .env file has been previously created (see environment variables)
2. Build image docker build -t <image-name> . with the desired image name
3. Use docker run --rm -p 8080:8000 --env-file .env <image-name> command, replacing image-name with the one built before
4. You can access the app in any web browser at http://127.0.0.1:8080/


From a DockerHub image
======================

**Download and install Docker Desktop**
1. First create the .env files (See environments variables section)
2. Go to the Docker repository: https://hub.docker.com/repository/docker/safo92150/oc_lettings/tags
3. Copy the tag you would like to use (preferably the most recent)
4. Use docker run --rm -p 8080:8000 --env-file .env safo92150/oc_lettings:<image-tag> command, replacing image-tag with the desired tag

**You can access the app in any web browser at http://127.0.0.1:8080/**

Quickstart
==========

**Once you clone the repository and files .env create, we need to make the migrations database:**

.. code-block::
 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py check

**Launch the application works locally:**

.. code-block::

    python manage.py runserver

**Do some tests**

.. code-block::

    python manage.py test

**Verify linting**


.. code-block::

    flake8

**Verify the test coverage and generate a html report**

.. code-block::

    pytest --cov=. --cov-report html


Admin dashboard
===============

**To access to the admin dashboard, go on admin login : http://127.0.0.1:8000/admin/**

.. image:: img/admin.png

To log:
username: **admin**
password: **Abc1234!** 

.. image:: img/login.png

**You are now on your dashboard and you can easily manage your data**

.. image:: img/dashboard.png

Reference `Installation`_.