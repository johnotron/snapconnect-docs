Uninstalling SNAP Connect
=========================

.. note:: To avoid spurious errors, close all running SNAPconnect applications while you uninstall.

Required for all versions
-------------------------

Kill all Python processes (may require admin privileges):

**In Linux:**

.. code:: sh

    killall python

**In Windows:**

.. code:: bat

    taskkill /F /IM python.exe

To uninstall from SNAP Connect 3.1.0
------------------------------------

SNAP Connect 3.1.0 installs to the site-packages folder:

**On Windows:**

-  ``C:\Python26\Lib\site-packages`` for Python 2.6
-  ``C:\Python27\Lib\site-packages`` for Python 2.7

**On Linux (including the E10):**

-  ``/usr/lib/python2.6/site-packages`` for Python 2.6
-  ``/usr/lib/python2.7/site-packages`` for Python 2.7

**Remove the following directories under your site-packages folder:**

-  ``apy``
-  ``serialwrapper``
-  ``snapconnect``
-  ``snaplib``

**Then remove the following file:**

-  ``snapconnect\*.egg-info``

For example, for Python 2.6 on Linux:

.. code:: sh

    rm -rf /usr/lib/python2.6/site-packages/apy
    rm -rf /usr/lib/python2.6/site-packages/serialwrapper
    rm -rf /usr/lib/python2.6/site-packages/snapconnect
    rm -rf /usr/lib/python2.6/site-packages/snaplib
    rm -rf /usr/lib/python2.6/site-packages/snapconnect*.egg-info

Python 2.6 in Windows (depending on where Python2.6 is installed this
could differ in your environment)

.. code:: bat

    rmdir /s /q C:\Python26\Lib\site-packages\apy
    rmdir /s /q C:\Python26\Lib\site-packages\serialwrapper
    rmdir /s /q C:\Python26\Lib\site-packages\snapconnect
    rmdir /s /q C:\Python26\Lib\site-packages\snaplib
    rmdir /s /q C:\Python26\Lib\site-packages\snapconnect*.egg-info

To uninstall from SNAP Connect 3.2.0
------------------------------------

SNAP Connect 3.2.0 installs to the site-packages folder:

**On Windows:**

-  ``C:\Python26\Lib\site-packages`` for Python 2.6
-  ``C:\Python27\Lib\site-packages`` for Python 2.7

**On Linux (including the E10):**

-  ``/usr/lib/python2.6/site-packages`` for Python 2.6
-  ``/usr/lib/python2.7/site-packages`` for Python 2.7

**Next, remove the following directories under your site-packages folder:**

-  ``apy``
-  ``serialwrapper``
-  ``snapconnect``
-  ``snaplayout``
-  ``snaplib``

**Then remove the following file:**

-  ``snapconnect\*.egg-info``

For example, for Python 2.6 on Linux:

.. code:: sh

    rm -rf /usr/lib/python2.6/site-packages/apy
    rm -rf /usr/lib/python2.6/site-packages/serialwrapper
    rm -rf /usr/lib/python2.6/site-packages/snapconnect
    rm -rf /usr/lib/python2.6/site-packages/snaplayout
    rm -rf /usr/lib/python2.6/site-packages/snaplib
    rm -rf /usr/lib/python2.6/site-packages/snapconnect*.egg-info

Python 2.6 in Windows (depending on where Python2.6 is installed this
could differ in your environment)

.. code:: bat

    rmdir /s /q C:\Python26\Lib\site-packages\apy
    rmdir /s /q C:\Python26\Lib\site-packages\serialwrapper
    rmdir /s /q C:\Python26\Lib\site-packages\snapconnect
    rmdir /s /q C:\Python26\Lib\site-packages\snaplayout
    rmdir /s /q C:\Python26\Lib\site-packages\snaplib
    rmdir /s /q C:\Python26\Lib\site-packages\snapconnect*.egg-info

To uninstall from SNAP Connect version 3.4.0 and later
------------------------------------------------------

SNAP Connect 3.4 installs via pip, so you’ll use pip to uninstall it:

.. code:: sh

    pip uninstall snapconnect