.. _Database:

========
Database
========


**The application use a SQLlite database for the data**

**This database contains 4 main tables:**

1. auth_user
2. lettings_letting
3. lettings_adresse
4. profiles_profile


.. image:: img/database-structure.png


The composition of the application's models:

+---------------+------------------+---------+
| Model         | Proprety         | Type    |
+===============+==================+=========+
| Adresse       | number           | int     |
+---------------+------------------+---------+
|               | street           | varchar |
+---------------+------------------+---------+
|               | city             | varchar |
+---------------+------------------+---------+
|               | zip_code         | varchar |
+---------------+------------------+---------+
|               | country_iso_code | varchar |
+---------------+------------------+---------+
| Letting       | title            | varchar |
+---------------+------------------+---------+
|               | address          | int     |
+---------------+------------------+---------+
| Profile       | user             | int     |
+---------------+------------------+---------+
|               | favorite_city    | varchar |
+---------------+------------------+---------+



Reference `Database`_.