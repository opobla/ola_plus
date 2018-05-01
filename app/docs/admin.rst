The Admin interface
==================

A very basic administration interface has been provided, mainly to manage the entities (HEI and LOS) and to manage
authorized users.


Accessing the admin panel
--------------------------

To access the administration panel browse to `http://api-location/admin`. The welcome screen will prompt for a username
and password. While regular users can read and write entities using the API, only users with the role *staff* are
allowed into the admin panel.

Managing users
--------------

Managing users is a very simple task. There are two kind of users: staff users and api users. Staff users are allowed
permission to access the admin panel and perform administrative operations, such as creating other users, issuing
tokens, managing entities, etc. API users are not allowed in the admin panel, but they have write permission on the
API, therefore they can post new HEI's and LOS's, define organizational units structure, etc.

The users and their operations are only available from the administration panel. They are not exposed in the API.