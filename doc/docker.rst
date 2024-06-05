.. _Docker:

======
Docker
======

For packaging the application is very simple. You need to have a DockerHub account.

First you need to download and install Docker Dekstop on the `Docker website <https://www.docker.com/products/docker-desktop/>`_

Second, sign up a DockerHub account at `DockerHub <https://hub.docker.com/>`_

Now for build an image and push to DockerHub: open a terminal at the root of the project.
You need to connect to DockerHub:

.. code-block::

    docker login --username "your dockerhub username" --password "your dockerhub password"

Second, you need to build the image:

.. code-block::

    docker build --tag "your dockerhub username"/"your image name" .

Third, you need to push the image on your DockerHub:

.. code-block::

    docker push "your dockerhub username"/"your image name"

If you want to run the app locally:

.. code-block::

    docker run -p "port to map":8000 "your dockerhub username"/"your image name"

Reference `Docker`_.
