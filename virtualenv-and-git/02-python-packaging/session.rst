Python packages
===============

We'll be talking about Python packages with more detail in a later
session.

Python packages are distributed as source or binary bundles of Python
code (binary packages may also include platform-specific shared
libraries, if C extensions were used).

Many Python packages are available from `PyPI`_, the Python package
index.


Inside a Python package
=======================

Python source packages are just directory structures, bundled in Zip or
Tar archives, which contain a top-level ``setup.py`` file describing its
contents.

Have a look at the `gribsloppy`_ toy package we developed a few sessions
ago, when we talked about generating Python bindings using ``ctypes``.

  .. _`PyPI`: http://pypi.python.org/
  .. _`gribsloppy`: https://github.com/carletes/gribsloppy
