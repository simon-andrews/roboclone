RoboClone |buildstatus| |pypiversion|
=========================================================================================================================================
A neat little script for cloning git repositories containing FRC robot projects
and configuring them for use with Eclipse.

Install Instructions
--------------------
Open a terminal and run::

   pip install roboclone

If you want the very latest version pushed to git then run::

   pip install git+https://github.com/simon-andrews/roboclone.git

Usage
-----
Now that you have RoboClone installed, it's time to use it! Open a terminal and type `roboclone`. Something like this
should show up::

   $ roboclone
   usage: roboclone [-h] [--gitargs args] [--force [FORCE]]
                    remote_url destination
   roboclone: error: the following arguments are required: remote_url, destination

Add the `-h` switch to show a help message::

   $ roboclone -h
   usage: roboclone [-h] [--gitargs args] [--force [FORCE]]
                    remote_url destination

   positional arguments:
     remote_url       url of the remote git repository (https or ssh)
     destination      directory to clone repository to

   optional arguments:
     -h, --help       show this help message and exit
     --gitargs args   extra arguments for git
     --force [FORCE]  write metadata files even if they already exist in the repo

Clone a repository::

   $ roboclone https://github.com/Team4761/2015-Robot-Code.git 2015-Robot-Code
   100%

.. |buildstatus| image:: https://img.shields.io/travis/simon-andrews/roboclone.svg
    :target: https://travis-ci.org/simon-andrews/roboclone

.. |pypiversion| image:: https://img.shields.io/pypi/v/roboclone.svg
    :target: https://pypi.python.org/pypi/roboclone/
