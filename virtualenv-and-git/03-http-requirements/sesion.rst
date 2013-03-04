Installing Python packages from URLs
====================================

Apart from specifying Python package names in your requirements file,
you may also use URLs pointing to Python packages.

Let's install now the Python package for ECMWF's web services API::

    (foo)carlos@elouard:~$ cat requirements.txt 
    # The ECMWF Python API client
    https://software.ecmwf.int/wiki/download/attachments/23694554/ecmwf-api-client-python.tgz

That Python package is available from https://software.ecmwf.int/, so let's use ``pip`` to install it,as before::

    (foo)carlos@elouard:~$ pip install -r requirements.txt 
    Downloading/unpacking https://software.ecmwf.int/wiki/download/attachments/23694554/ecmwf-api-client-python.tgz (from -r requirements.txt (line 2))
      Downloading ecmwf-api-client-python.tgz
      Running setup.py egg_info for package from https://software.ecmwf.int/wiki/download/attachments/23694554/ecmwf-api-client-python.tgz
    
    Installing collected packages: ecmwf-api-client
      Running setup.py install for ecmwf-api-client
    
    Successfully installed ecmwf-api-client
    Cleaning up...
    (foo)carlos@elouard:~$

Now the ECMWF API modules are available::

    (foo)carlos@elouard:~$ python
    Python 2.7.3 (default, Sep 26 2012, 21:51:14) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import ecmwfapi
    >>> ecmwfapi.__version__
    '1.1'
    >>> 
    (foo)carlos@elouard:~$
