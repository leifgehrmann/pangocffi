# How to contribute

Thanks for reading!

You can help by:

* Reporting any issues and requesting enhancements,
* Updating documentation, or...
* Modifying code and submitting a pull request.

## Reporting issues and requesting enhancements

Issues and enhancements can be reported on [pangocffi issues on GitHub].

[pangocffi issues on GitHub]: https://github.com/leifgehrmann/pangocffi/issues/new).

## Modifying documentation

Any changes to the documentation can be generated and viewed:

```bash
$ make docs
```

## Modifying code

You'll first need to setup a development environment. You will need to install
the following

Then run the following:

```bash
    $ pip install setuptools
    $ pip install -r requirements.txt
```

### Testing code changes

A quick test can be done by running:

```bash
    $ make tests
```

But for completeness, it's recommended to run tests for *all* python
interpreters using tox:

```bash
    $ make tests-all
```

### Formatting

This repository uses [flake8] to enforce various linting rules. To check your
code complies, run:

```bash
    $ make lint
```

[flake8]: https://gitlab.com/pycqa/flake8

## Making a new release

This project uses SemVer for managing version numbers. The version number in
the file `pangocffi/VERSION` should be updated, and committed before a new
release.

After this change has been merged into master, a new release on GitHub should
be made. Changes in the release should be added to the Releases section on
GitHub.

Finally, with the tagged version checked out on a machine, run the following:

```bash
$ make release
```

This command will prompt for username and password of the PyPi account. Making
a release requires credentials of the project owner. If you would like to be
co-owner of the project, do not hesitate to ask!
