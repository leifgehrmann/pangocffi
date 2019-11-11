How to contribute
=================

Thanks for reading!

You can help by:

* Reporting any issues and requesting enhancements,
* Updating documentation, or...
* Modifying code and submitting a pull request.

Reporting issues and requesting enhancements
--------------------------------------------

Issues and enhancements can be reported on `pangocffi issues on GitHub`_.

.. _pangocffi issues on GitHub: https://github.com/leifgehrmann/pangocffi/issues/new).

Modifying documentation
-----------------------

Documentation can be generated and viewed::

    $ make docs

Modifying code
--------------

You'll first need to setup a development environment. You will need to install
the following

Then run the following::

    $ pip install setuptools
    $ pip install -r requirements.txt

Testing code changes
~~~~~~~~~~~~~~~~~~~~

A quick test can be done by running::

    $ make tests

But for completeness, it's recommended to run tests for *all* python
interpreters using tox::

    $ make tests-all

Formatting
~~~~~~~~~~

This repository uses flake8_ to enforce various linting rules. To check your
code complies, run::

    $ make lint

.. _flake8: https://gitlab.com/pycqa/flake8

Making a new release
--------------------

Any changes should be reported in ``NEWS.rst``.

Running the following command will prompt for username and password of the PyPi
account::

    $ make release

Making a release requires credentials of the project owner. If you would like
to be co-owner of the project, do not hesitate to ask!
