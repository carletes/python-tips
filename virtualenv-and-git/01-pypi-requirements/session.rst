Installing Python packages in a virtualenv
==========================================

The command ``pip`` lets you install Python packages::

    (foo)carlos@elouard$ which pip
    /home/carlos/.virtualenvs/foo/bin/pip
    (foo)carlos@elouard$ 

Let's have a look at what gets installed by default::

    (foo)carlos@elouard$ pip freeze
    argparse==1.2.1
    distribute==0.6.24
    wsgiref==0.1.2
    (foo)carlos@elouard$ 

Not much --- just a few dependencies of ``virtualenv`` itself. You can
now install any Python you need. Let's grab Django, for instance::

    (foo)carlos@elouard$ pip install Django
    Downloading/unpacking Django
      Downloading Django-1.5.tar.gz (8.0Mb): 8.0Mb downloaded
      Running setup.py egg_info for package Django
    
        warning: no previously-included files matching '__pycache__' found under directory '*'
        warning: no previously-included files matching '*.py[co]' found under directory '*'
    Installing collected packages: Django
      Running setup.py install for Django
        changing mode of build/scripts-2.7/django-admin.py from 644 to 755
    
        warning: no previously-included files matching '__pycache__' found under directory '*'
        warning: no previously-included files matching '*.py[co]' found under directory '*'
        changing mode of /home/carlos/.virtualenvs/foo/bin/django-admin.py to 755
    Successfully installed Django
    Cleaning up...
    (foo)carlos@elouard$ 

Django is now installed under your current virtualenv::

    (foo)carlos@elouard$ pip freeze
    Django==1.5
    argparse==1.2.1
    distribute==0.6.24
    wsgiref==0.1.2
    (foo)carlos@elouard$

We did not specify any version for Django, so we get by default the latest one.

The Django distribution, in particular, includes a script to manage Django web
application. That script, caled ``django-admin.py``, is now available in our
virtualenv::

    (foo)carlos@elouard$ which django-admin.py
    /home/carlos/.virtualenvs/foo/bin/django-admin.py
    (foo)carlos@elouard$ django-admin.py --help
    Usage: django-admin.py subcommand [options] [args]

    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Print traceback on exception
      --version             show program's version number and exit
      -h, --help            show this help message and exit
    
    Type 'django-admin.py help <subcommand>' for help on a specific subcommand.
    
    Available subcommands:
    
    [django]
        cleanup
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        runfcgi
        runserver
        shell
        sql
        sqlall
        sqlclear
        sqlcustom
        sqlflush
        sqlindexes
        sqlinitialdata
        sqlsequencereset
        startapp
        startproject
        syncdb
        test
        testserver
        validate
    (foo)carlos@elouard$ 


The requirements file
=====================

You may list all Python packages you need for a project you're working
on in a text file, usually called ``requirements.txt``, so that you (and
other people) can initialise a virtual environment with a single
command.

Imagine you need to develop a Django web application backed by a MySQL
database. You would need the following Python packages:

* Dango itself
* The MySQL drivers for Python

Your ``requirements.txt`` file would look like this::

    (foo)carlos@elouard$ cat requirements.txt 
    # Django
    Django
    
    # MySQL drivers
    MySQL-python
    (foo)carlos@elouard$ 

You may pass now the name of your requirements file to ``pip``, and then
``pip`` will install any packages you don't have yet::

    (foo)carlos@elouard$ pip install -r requirements.txt 
    Requirement already satisfied (use --upgrade to upgrade): Django in
    /home/carlos/.virtualenvs/foo/lib/python2.7/site-packages (from -r
    requirements.txt (line 2))
    Downloading/unpacking MySQL-python (from -r requirements.txt (line 5))
      Downloading MySQL-python-1.2.4.zip (113Kb): 113Kb downloaded
      Running setup.py egg_info for package MySQL-python
    
    Installing collected packages: MySQL-python
      Running setup.py install for MySQL-python
        building '_mysql' extension
        gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -Dversion_info=(1,2,4,'final',1) -D__version__=1.2.4 -I/usr/include/mysql -I/usr/include/python2.7 -c _mysql.c -o build/temp.linux-x86_64-2.7/_mysql.o -DBIG_JOINS=1 -fno-strict-aliasing -g
        In file included from _mysql.c:44:0:
        /usr/include/mysql/my_config.h:422:0: warning: "HAVE_WCSCOLL" redefined [enabled by default]
        In file included from /usr/include/python2.7/Python.h:8:0,
                         from _mysql.c:29:
        /usr/include/python2.7/pyconfig.h:890:0: note: this is the location of the previous definition
        gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-x86_64-2.7/_mysql.o -L/usr/lib/x86_64-linux-gnu -lmysqlclient_r -lpthread -lz -lm -lrt -ldl -o build/lib.linux-x86_64-2.7/_mysql.so
    
    Successfully installed MySQL-python
    Cleaning up...
    (foo)carlos@elouard$
