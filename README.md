Whiskerboard
============

Whiskerboard is a status board for websites, services and APIs, like Amazon's [AWS status page](http://status.aws.amazon.com/).

It is heavily based on [Stashboard](http://www.stashboard.org/). Unlike Stashboard, it uses vanilla Django, so you aren't stuck using Google App Engine.


Quick start guide
-----------------

    $ git clone git@github.com:sijis/whiskerboard.git
    $ cd whiskerboard
    $ sudo pip install -r requirements.txt
    $ Add a "SECRET_KEY = 'EnterABunchOfRandomCharactersHere'" to settings/base.py
        (Alternatively, use http://www.miniwebtool.com/django-secret-key-generator/ to create a secret key!)
    $ ./manage.py syncdb
    $ ./manage.py migrate
    $ ./manage.py runserver

You might need to install [pip](http://www.pip-installer.org/en/latest/installing.html).
Back on the admin home page, click on "services" and add the things you want to report the status of (website, API etc).
To change the status of a service add an event for it.

API Documentation
-----------------

Visit the [wiki](http://github.com/sijis/whiskerboard/wiki) page on details about the API.

You may also find useful the [whiskerboard-tools](http://github.com/sijis/whiskerboard-tools) repository.

