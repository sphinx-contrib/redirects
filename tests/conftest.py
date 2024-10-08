"""
    pytest config for sphinxcontrib/redirects/tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by Stephen Finucane <stephen@that.guru>
    :license: BSD, see LICENSE for details.
"""

import pathlib
import shutil

import pytest

# this is necessary because Sphinx isn't exposing its fixtures
# https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html#requiring-loading-plugins-in-a-test-module-or-conftest-file
pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture
def rootdir(tmpdir):
    src = pathlib.Path(__file__).parent.resolve() / 'roots'
    dst = tmpdir.join('roots')
    shutil.copytree(src, dst)
    roots = pathlib.Path(dst)
    yield roots
    shutil.rmtree(dst)
