Python packages from Git URLs
=============================

We may also tell ``pip`` to install Python packages from Git URLs. Let's
install our ``gribsloppy`` package, whose Git URL is
https://github.com/carletes/gribsloppy.git::

    (foo)carlos@elouard$ cat requirements.txt 
    git+https://github.com/carletes/gribsloppy.git#egg=gribsloppy
    (foo)carlos@elouard$ pip install -r requirements.txt 
    Downloading/unpacking gribsloppy from git+https://github.com/carletes/gribsloppy.git (from -r requirements.txt (line 1))
      Cloning https://github.com/carletes/gribsloppy.git to /home/carlos/.virtualenvs/foo/build/gribsloppy
      Running setup.py egg_info for package gribsloppy
        
        warning: no files found matching 'README.rst'
    Installing collected packages: gribsloppy
      Running setup.py install for gribsloppy
        
        warning: no files found matching 'README.rst'
    Successfully installed gribsloppy
    Cleaning up...
    (foo)carlos@elouard$

Our ``gribsloppy`` package is now available::

    (foo)carlos@elouard$ python
    Python 2.7.3 (default, Sep 26 2012, 21:51:14) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import gribsloppy
    >>> gribsloppy.__version__
    '0.1.0'
    >>> gribsloppy.__file__
    '/home/carlos/.virtualenvs/foo/local/lib/python2.7/site-packages/gribsloppy/__init__.pyc'
    >>> 
    (foo)carlos@elouard$ 
