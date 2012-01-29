Appsembler wrapper for djangotutorial
=====================================

This project is an example of how to create a wrapper for deploying a simple Django project using Appsembler.

The project consists of:

 * stackato.yml
 * wsgi.py
 * requirements.pip
 * settings.py
 * djangotutorial (this is checked out as a git submodule - see below)

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

See the Github help for more info about `working with submodules <http://help.github.com/submodules/>`_