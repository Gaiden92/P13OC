.. _Installation:

============
Installation
============

**This section will help you to install the application:**

+ from a Gitlab repository
+ with building an image of the app and run it with Docker
+ from a Docker Hub image

Environments variables
======================

**First create a .env files for add the environments variables:
Create a '.env' files at the project root and copy paste this code:**

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

From a Gitlab repository
======================

**Requirements**

In order to use the pipeline CI/CD, you will need these prerequisites:

1. **Python** install on your pc for launch the command.
2. **Git** install on your pc for the git clone command.

**Open a shell and type this command on your terminal to clone the project:**

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

**Once you clone the repository and file .env create, we need to make the migrations database:**

.. code-block::
 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py check

**Launch the application works locally:**

.. code-block::

    python manage.py runserver


You can now access to the application in any web browser at http://127.0.0.1:8080/


Build a Docker image to run the application locally
===================================================

**Requirements**

1. **Python** install on your pc for launch the command.
2. **Git** install on your pc for the git clone command.
3. **Docker** install on your pc to build and run the image. 


**Download and install Docker Dekstop**

Change to the project directory cd /path/to/OC_LETTINGS

1. Do the same step that the Installation from a Gitlab repository until the Sentry part. 
2. Make sure that the .env file has been previously created (see environment variables)
3. Build image docker build -t <image-name> . with the desired image name
4. Use docker run --rm -p 8080:8000 --env-file .env <image-name> command, replacing image-name with the one built before

You can access the application in any web browser at http://127.0.0.1:8080/


From a DockerHub image
======================

**Requirements**

1. **Python** install on your pc for launch the command.
2. **Git** install on your pc for the git clone command.
3. **Docker** install on your pc to build and run the image. 

**Download and install Docker Desktop**

1. First create the .env files (See environments variables section)
2. Go to the Docker repository: https://hub.docker.com/repository/docker/safo92150/oc_lettings/tags
3. Copy the tag you would like to use (preferably the most recent)
4. Use docker run --rm -p 8080:8000 --env-file .env safo92150/oc_lettings:<image-tag> command, replacing image-tag with the desired tag

You can access the application in any web browser at http://127.0.0.1:8080/


Quickstart
==========


**Until you can launch the application with this command:**

.. code-block::
    
    python manage.py runserver

**You can now go on the homepage at http://127.0.0.1:8000/ and search some lettings.**

.. image:: img/home.png


Admin dashboard
===============

**To access to the admin dashboard, go on admin login : http://127.0.0.1:8000/admin/**

.. image:: img/admin.png

To log:

* username: admin
* password: Abc1234! 

.. image:: img/login.png
    :align: center

**You are now on your dashboard and you can easily manage your data**

.. image:: img/dashboard.png

Reference `Installation`_.