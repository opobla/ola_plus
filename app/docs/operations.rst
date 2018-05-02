.. _linking-pages:

Operations
==========

In this section we will explain the basic operations that are defined on the HEI's and LOS, and how can they be
performed from :ref:`the admin interface <admin-interface>` or from the :ref:`the API <api-swagger>`.

Please, note that in all the following examples the API url and the token used are ``http://0.0.0.0:8000``
and ``ceaaa8b61ea64a710779b4a61b29aa4c3dd98f76`` respectively. You need to change both of them accordingly to your
environment, as this two are just examples. Also note that the JSON in the payload has been escaped so it works when
it is call from a shell. This might change depending on your programming language and framework.


Creating a HEI
--------------

New HEI can be created from :ref:`the admin interface <admin-interface>` or by using the following curl code

.. code-block:: bash

    curl -X POST "http://0.0.0.0:8000/api/hei" -H "accept: application/json"
        -H "Authorization: Token ceaaa8b61ea64a710779b4a61b29aa4c3dd98f76"
        -H "Content-Type: application/json"
        -d "{
            \"name\": \"University of Alcalá\",
            \"email\": \"antonio.guerrero@uah.es\"
        }"


Getting all the existing HEI
----------------------------
All the HEI can be retrieved by using the following curl command:

.. code-block:: bash

    curl -X GET "http://0.0.0.0:8000/api/hei" -H "accept: application/json"

Optionally, a query param can be given, for example ``?q=alca`` that will filter out all the HEI whose name contains
the sequence ``alca``.


Adding an organizational unit
-----------------------------

Organizational units can be added one by one or by nesting them all in an array. The following example shows how to
add an organizational unit the Polytechnic school of the University of Alcalá. To make this call it is necessary to
have the ID's of both, the HEI and the existing OUNIT. The HEI identifiers can be obtained by calling the GET ``/hei``
method, that yields ``52fcb1df-5ab8-4703-b582-368c609f36ea``, and the second by calling with this ID to
GET ``/hei/52fcb1df-5ab8-4703-b582-368c609f36ea``. This last call is very useful to download the hierarchical structure
of the HEI when filling the corresponding web form. For example, the Polytechnic school has the ID
``b42b39f3-f11a-4c87-97b6-399945a8a343``. This all this data we can finally add the new organizational unit.


.. code-block:: bash

    curl -X POST "http://0.0.0.0:8000/api/hei/5e4bd4ac-c14b-4c57-8573-5ad60a7eff0c"
        -H "accept: application/json"
        -H "Content-Type: application/json"
        -H "Authorization: Token ceaaa8b61ea64a710779b4a61b29aa4c3dd98f76"
        -d "{
            \"ounits\": [ {
                \"name\": \"Theory of the Signal Department\",
                \"code\": \"TEOSE\",
                \"higher_education_institution\": \"5e4bd4ac-c14b-4c57-8573-5ad60a7eff0c\",
                \"parent\": \"b42b39f3-f11a-4c87-97b6-399945a8a343\"
            } ]}"

Adding a Learning Opportunity associated with a OUNIT
-----------------------------------------------------

Learning Opportunities can be created from the admin page or from the API. To create a LOS a call to POST ``/api/los``,
for example:

.. code-block:: bash

    curl -X POST "http://0.0.0.0:8000/api/los"
        -H "accept: application/json"
        -H "Authorization: Token ceaaa8b61ea64a710779b4a61b29aa4c3dd98f76"
        -H "Content-Type: application/json"
        -d "{
            \"code\": \"78007\",
            \"title\": \"Operating Systems\",
            \"area\": \"ATC1\",
            \"isced_code\": \"ISCET1234\",
            \"credit_scheme\": \"ECTS\",
            \"credit_value\": 6,
            \"academic_term\": \"First Semester\",
            \"start_date\": \"2019-09-01\",
            \"end_date\": \"2020-01-31\",
            \"organizational_unit\": \"b3e24a6f-2b2e-4fd7-a500-c4570d2778b7\"
        }"

The ``organizational_unit`` can be any organizational unit, independently from is hierarchical level, although the
typical should be a third level organizational unit. That is, given the basic schema HEI->FACULTY->DEPARTMENT, LOS
should be associated with the departments, but it is not mandatory.

Obtaining LOS filters
---------------------

This feature is heavily oriented to web-based search facilities. This service returns all the different alternatives
of the value of an attribute, this in turn is used to offer the possibility to filter by this value. For example, let's
pretend that the result of GET ``/los/filter`` is the following:

.. code-block:: json

    {
        "academic_term": [
            "First Semester",
            "Second Semester"
        ],
        "credit_value": [
            6,
            12
        ]
    }

This means that all the LOS are either of the "First Semester" or of the "Second Semester", and also that all the LOS
have 6 or 12. With this information the web page can build the corresponding filters, for example:

.. image:: img/Samplefilter.png
   :alt: alternate text
   :align: center


Filtering LOS
-------------

LOS can be filtered with different criteria: ``title`` (partial search supporter, i.e "sys" -> Operating Systems),
``isced_code``, ``credit_value``, ``academic_term``, etc (see the :ref:`the API <api-swagger>`). For example,
to filter all the LOS with 6 credits of the organizational unit with id ``b3e24a6f-2b2e-4fd7-a500-c4570d2778b7``
you can use curl this way:

.. code-block:: bash
    :emphasize-lines: 1

    curl -X GET "http://0.0.0.0:8000/api/los/b3e24a6f-2b2e-4fd7-a500-c4570d2778b7?credit_value=6"
        -H "accept: application/json"


