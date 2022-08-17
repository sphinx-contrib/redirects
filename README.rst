=======================
sphinxcontrib-redirects
=======================

This contrib extension, `sphinxcontrib.redirects`, provides a Sphinx extension
for generating JavaScript-driven redirects for moved pages. It currently only
supports the `html` builder (``sphinx.builders.html.SingleFileHTMLBuilder``).

.. note::

    The `sphinxext-rediraffe <https://pypi.org/project/sphinxext-rediraffe/>`__
    extension appears to provide many more features that this package and
    should probably be preferred for new projects.

Usage
-----

To enable the extension, you should add it to your ``conf.py`` file::

    extensions = [
        'sphinxcontrib.redirects',
        ...
    ]

The extension relies on a *redirect file*. This defaults to ``redirects``
within the source directory but it can be overridden. To override this value,
add the following to your ``conf.py`` file::

    redirects_file = '<path to redirects file>'

The *redirect file* is a simple space-separated file of ``old_path`` -
``new_path`` pairs. These paths are relative to the source directory and should
include their extension. For example, if you renamed the file ``test.rst`` to
``testing.rst`` then you could write::

    test.rst testing.rst

This works for files moved between directories too. If you moved a ``test.rst``
to ``testing/index.rst`` instead, then you could write::

    test.rst testing/index.rst

For examples, refer to the samples used in the `tests
<tests/roots>`__.

Contributing
------------

For information on contributing, refer to the `contributing guide
<CONTRIBUTING.rst>`__.
