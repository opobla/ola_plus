.. _api-swagger:
.. _swagger_url: http://ola.i2tic.com

==================
The API swagger
==================

The API is self-documented using swagger. The swagger is a web page intended for testing and developing that enumerates,
describes and tests the services exported by the API.

.. image:: img/swagger-front-page.png
   :width: 400px
   :alt: alternate text
   :align: right


To access this page browse to |swagger_url|. Every service can be
tested individually, but bear in mind that write-oriented services, such as POST, PUT or DELETE require the user to
be authenticated by means of a token. See :ref:`using-token-swagger`

Basic GET operations
--------------------

To show how to use swagger, we will use the service ``/hei`` to obtain a list of all the Higher Education Institutions
available. Click anywhere inside the ``[GET]/hei`` service to unfold the section:

.. image:: img/get-hei-service.png
   :alt: alternate text
   :align: center


This services can be parametrized with some values, but they are not required for this example. Just press
the "Execute" button to request the service. Bellow, in the "Server response" there will be the JSON document with the
results.

.. _using-token-swagger:

Using an authorization token
----------------------------

To obtain a token ask for it to your administrator, or if your are a staff user, then
log in the admin panel in |admin_url| and follow the instructions to
:ref:`obtain a authentication token <managing-authentication-tokens>`.

An authentication token is a hash key that looks like ``ceaaa8b61ea64a710779b4a61b29aa4c3dd98f76``. To use this token
in the swagger, use the button "Authorized". It will open a popup window with just a box labeled "Value". In this box
type the word ``Token`` followed by a space and then paste the authentication token, for example:
``Token ceaaa8b61ea64a710779b4a61b29aa4c3dd98f76``. Finally press "Autorize" and close the popup. From now on, all
the requests will include the authorization token.