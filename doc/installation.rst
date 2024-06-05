.. _Installation:

============
Installation
============


Clone the project on your local machine
=======================================

**Type this command on your terminal to clone the project:**

.. code-block::

    git clone 'https://gitlab.com/sf5810217/oc_lettings.git'


Run in local
============

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

**Finally, we must to create a .env files for the configuration settings:
Create a '.env' files and copy paste this code:**

.. code-block::

    SECRET_KEY = "yoursecretkey"
    DSN = "your dsn sentry"
    DJANGO_DEBUG = 'True'
    ALLOWED_HOSTS = ['*']

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

Reference `Installation`_.