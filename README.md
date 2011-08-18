Whiskerboard
============

Whiskerboard is a status board for websites, services and APIs, like Amazon's [AWS status page](http://status.aws.amazon.com/).

It is heavily based on [Stashboard](http://www.stashboard.org/). Unlike Stashboard, it uses vanilla Django, so you aren't stuck using Google App Engine.

Have a look at the demo: [http://whiskerboard.ep.io/](http://whiskerboard.ep.io/).

Quick start guide
-----------------

    $ git clone git@github.com:victortrac/whiskerboard.git
    $ cd whiskerboard
    $ sudo pip install -r requirements.txt
    $ echo "SECRET_KEY = 'EnterABunchOfRandomCharactersHere'" > settings/local.py
    $ ./manage.py syncdb
    $ ./manage.py runserver

You might need to install [pip](http://www.pip-installer.org/en/latest/installing.html).

Back on the admin home page, click on "services" and add the things you want to report the status of (website, API etc). To change the status of a service add an event for it.


