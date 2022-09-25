.. ch-orm documentation master file, created by
   sphinx-quickstart on Sun Sep 25 11:21:13 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Overview
==================================

This project is simple ORM for working with the [ClickHouse database](https://clickhouse.tech/). It allows you to define model classes whose instances can be written to the database and read from it.

This repository is expected to use more type hints and only supports Python 3.7+.

Supports both synchronous and asynchronous ways to interact with the clickhouse server. Means you can use asyncio to perform asynchronous queries.

To install ch-orm:

.. code-block:: bash

    pip install ch-orm

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   models_and_databases
   async_databases
   expressions
   querysets
   field_options
   field_types
   table_engines
   schema_migrations
   system_models
   contributing
   class_reference


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
