Managing virtual environments
=============================

Virtualenvs are created with the ``mkvirtualenv`` command::

    carlos@elouard:~$ mkvirtualenv foo
    New python executable in foo/bin/python
    Installing
    distribute.............................................................................................................................................................................................done.
    Installing pip...............done.
    virtualenvwrapper.user_scripts creating /home/carlos/.virtualenvs/foo/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/carlos/.virtualenvs/foo/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/carlos/.virtualenvs/foo/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/carlos/.virtualenvs/foo/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/carlos/.virtualenvs/foo/bin/get_env_details
    (foo)carlos@elouard:~$ 

Notice the ``(foo)`` prefix in the shell prompt. It means that now we're
running under the virtualenv called ``foo``::

    (foo)carlos@elouard:~$ which python
    /home/carlos/.virtualenvs/foo/bin/python
    (foo)carlos@elouard:~$ 

You can create as many virtualenvs as you need::

    (foo)carlos@elouard:~$ mkvirtualenv bar
    New python executable in bar/bin/python
    [..]
    (bar)carlos@elouard:~$ which python
    /home/carlos/.virtualenvs/bar/bin/python
    (bar)carlos@elouard:~$ 

When you have several virtualenvs, you may switch among them::

    (bar)carlos@elouard:~$ workon foo
    (foo)carlos@elouard:~$ workon bar
    (bar)carlos@elouard:~$ 

You may also deactivate your current virtualenv::

    (bar)carlos@elouard:~$ deactivate 
    carlos@elouard:~$ 

When you don't need a virtualenv any longer, you may also delete it::

    carlos@elouard:~$ rmvirtualenv foo
    Removing foo...
    carlos@elouard:~$ rmvirtualenv bar
    Removing bar...
    carlos@elouard:~$ 

Inside a virtualenv
===================

The command ``mkvirtualenv`` creates a self-contained Python
distribution under ``$WORKON_HOME``::

    carlos@elouard:~$ mkvirtualenv foo
    New python executable in foo/bin/python
    [..]
    (foo)carlos@elouard:~$

You can inspect the contents of your virtualenv with the
``cdvirtualenv`` command::

    (foo)carlos@elouard:~$ cdvirtualenv 
    (foo)carlos@elouard:~/.virtualenvs/foo$ ls
    bin  include  lib  local
    (foo)carlos@elouard:~/.virtualenvs/foo$ ls bin/
    activate       activate_this.py  get_env_details  postactivate
    predeactivate
    activate.csh   easy_install      pip              postdeactivate  python
    activate.fish  easy_install-2.7  pip-2.7          preactivate
    (foo)carlos@elouard:~/.virtualenvs/foo$ 
