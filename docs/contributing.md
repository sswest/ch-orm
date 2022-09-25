Contributing
============

This project is hosted on GitHub - [https://github.com/sswest/ch-orm](https://github.com/sswest/ch-orm).

Please open an issue there if you encounter a bug or want to request a feature.
Pull requests are also welcome.

Building
--------

After cloning the project, run the following commands:

```shell
pip install build
python -m build
```

A `dist` directory will be generated, which you can use to install the development version of the package:

```shell
pip install dist/*
```

Tests
-----

To run the tests, ensure that the ClickHouse server is running on <http://localhost:8123/> (this is the default), and run:

```shell
python -m unittest
```

To see test coverage information run:

```shell
coverage run --source=clickhouse_orm -m unittest
coverage report -m
```
