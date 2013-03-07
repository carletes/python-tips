A real-world example: Our virtualenv for running ECMWF web applications
=======================================================================

This is the output of ``pip freeze`` for the virtualenv we use to run
our Django-based web applications::

    Django==1.4.3
    Markdown==2.2.1
    MySQL-python==1.2.4
    PyYAML==3.10
    Twisted==12.3.0
    amqp==1.0.8
    anyjson==0.3.3
    billiard==2.7.3.21
    celery==3.0.15
    coverage==3.6
    distribute==0.6.34
    django-celery==3.0.11
    django-jsonfield==0.8.12
    django-mptt==0.5.5
    django-pjax==1.2
    django-polymorphic==0.2
    -e git+https://software.ecmwf.int/stash/scm/WEB/ecpc.git@e0e5405b0db9147fdcf714933b2562a35bdded21#egg=ecpc-dev
    feedparser==5.1.3
    flup==1.0.3.dev-20110405
    httplib2==0.7.7
    ipaddr==2.1.10
    johnny-cache==1.4
    kombu==2.5.6
    lxml==3.1.0
    -e git+https://software.ecmwf.int/stash/scm/ECCHARTS/mockecmwf.git@033b7777fa2f71d740b37a08a1d6a921d4c55d00#egg=mockecmwf-dev
    protobuf==2.5.0
    psycopg2==2.4.6
    pymongo==2.4.2
    python-dateutil==1.5
    python-ldap==2.4.10
    -e git+https://software.ecmwf.int/stash/scm/WEBMARS/python-mars.git@0730c715164bd518669293381e8316774c6d1f9f#egg=python_mars-dev
    python-memcached==1.48
    pytz==2012j
    rethinkdb==1.2.6-2
    -e git+https://software.ecmwf.int/stash/scm/ECCHARTS/servicelib.git@0c53629b0a889f71ef884b5cf1e4ed17c2c88354#egg=servicelib-dev
    stomper==0.2.4
    -e git+https://software.ecmwf.int/stash/scm/ECCHARTS/web-components.git@61dec07f937264f1a126391188014e78b3b9b668#egg=web_components-dev
    webauth==2.5.2
    -e git+https://software.ecmwf.int/stash/scm/ECCHARTS/wreptools.git@41ae41393e6d63e8f5ad12164c3ebe4664f7319d#egg=wreptools-dev
    wsgiref==0.1.2
    zope.interface==4.0.3
