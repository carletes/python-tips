Editable Git packages
=====================

The most interesting feature of installing Python packages from Git
repositories is that you may receive updates to them.

Let's import our ``gribsloppy`` package in editable mode::

    (foo)carlos@elouard$ cat requirements.txt 
    -e git+https://github.com/carletes/gribsloppy.git#egg=gribsloppy
    (foo)carlos@elouard$

(Notice the ``-e`` prefix to the Git URL). Now, when we install it,
``pip`` will do a Git checkout of the source code, and make the package
available to us::

    (foo)carlos@elouard$ pip install -r requirements.txt 
    Obtaining gribsloppy from git+https://github.com/carletes/gribsloppy.git#egg=gribsloppy (from -r requirements.txt (line 1))
      Cloning https://github.com/carletes/gribsloppy.git to /home/carlos/.virtualenvs/foo/src/gribsloppy
      Running setup.py egg_info for package gribsloppy
        
        warning: no files found matching 'README.rst'
    Installing collected packages: gribsloppy
      Running setup.py develop for gribsloppy
        
        warning: no files found matching 'README.rst'
        Creating /home/carlos/.virtualenvs/foo/lib/python2.7/site-packages/gribsloppy.egg-link (link to .)
        Adding gribsloppy 0.1.0 to easy-install.pth file
        
        Installed /home/carlos/.virtualenvs/foo/src/gribsloppy
    Successfully installed gribsloppy
    Cleaning up...
    (foo)carlos@elouard$ 

Now ``pip`` has used ``git`` to check out the source code of ``gribsloppy``
under ``$WORKON_HOME/foo/src/gribsloppy``::

    (foo)carlos@elouard$ cdvirtualenv src/gribsloppy
    (foo)carlos@elouard$ ls
    gribsloppy           Makefile     requirements-devel.txt
    gribsloppy.egg-info  MANIFEST.in  setup.py
    (foo)carlos@elouard$ git status
    # On branch master
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #       gribsloppy.egg-info/
    nothing added to commit but untracked files present (use "git add" to track)
    (foo)carlos@elouard$ 

Imagine someone makes a change to ``gribsloppy``. We can then now get
the latest fixes using ``git``::

    (foo)carlos@elouard$ git pull origin master
    remote: Counting objects: 7, done.
    remote: Compressing objects: 100% (4/4), done.
    Unpacking objects: 100% (4/4), done.
    remote: Total 4 (delta 2), reused 0 (delta 0)
    From https://github.com/carletes/gribsloppy
     * branch            master     -> FETCH_HEAD
    Updating cd82a11..d884022
    Fast-forward
     gribsloppy/__init__.py |    2 +-
     1 file changed, 1 insertion(+), 1 deletion(-)
    (foo)carlos@elouard$ 

And it works::

    (foo)carlos@elouard$ python
    Python 2.7.3 (default, Sep 26 2012, 21:51:14) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import gribsloppy
    >>> gribsloppy.__version__
    '0.1.1'
    >>> 
    (foo)carlos@elouard$
