==========
Quickstart
==========

Once you clone the repository and files .env create, we need to make the migrations database:
.. code-block::
    python manage.py makemigrations
    python manage.py migrate
    python manage.py check

Launch the application works locally:
.. code-block::
    python manage.py runserver

Make some tests
===============
.. code-block::
    python manage.py tests

Verify linting
==============
.. code-block::
    flake8

Verify the test coverage and generate a html report
=========================
.. code-block::
    pytest --cov=. --cov-report html