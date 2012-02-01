Appsembler wrapper for djangotutorial
=====================================

This project is an example of how to create a wrapper for deploying a simple Django project using Appsembler.

The project consists of:

 * stackato.yml
 * wsgi.py
 * requirements.pip (these are install automatically by pip)
 * appsembler_settings.py (necessary overrides)
 * djangotutorial (this is checked out as a git submodule - see below)

Copy appsembler_settings file
-----------------------------

Copy the appsembler_settings.py file into the ``mysite`` directory::

    $ cp appsembler_settings.py mysite
    
This will be done automatically by our web-based deploy process, but when using the command line, it needs to be done manually.

Cloning this repo
-----------------

Since this project uses Git submodules, you should clone it using ``--recursive``::

    $ git clone --recursive git://github.com/appsembler/djangotutorial_appsembler.git
 
If you need to update the code from this repository, you simple run these commands::

    $ git submodule init
    $ git submodule update

Adding the djangotutorial repo as a submodule
---------------------------------------------

If you want to add your own git submodules, you can follow these steps. Rather than making a copy of the djangotutorial repo, we simple define a pointer to it using the Git submodule technique::

    $ git submodule add git://github.com/appsembler/djangotutorial.git mysite

You should now have a directory ``mysite`` which contains the cloned repository djangotutorial.

See the Github help for more info about `working with submodules <http://help.github.com/submodules/>`_ and `this blog post <http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/>`_

Deploying to Appsembler
-----------------------

You can deploy this app to Appsembler with just a few commands. First download the Stackato command line tool from http://community.activestate.com/stackato/download

Then you can deploy it the first time with::

    $ stackato target http://api.somedomain.com
    $ stackato login --email name@domain.com --password *****
    $ stackato push

The next time you need to deploy, you use the update command::

    $ stackato update
