Installing SNAP Connect
=======================

Requirements
------------
Be sure to load these before installing the package:

* `Python <https://www.python.org/downloads/>`_ 2.6 or 2.7
* `pip <https://pip.pypa.io/en/stable/installing/>`_ 8.1 or later
* `PyCrypto <http://pycrypto.org/>`_ (optional - if AES-128 support is required)

Install via pip
---------------
This is the recommended way to install *SNAP Connect*

.. code-block:: bash

    pip install -i https://update.synapse-wireless.com/pypi snapconnect

Install offline
---------------
To cache the download to transfer via USB key, run the following as a single command:

.. code-block:: bash

    pip install --download=”/mypathtosave/” \
      –i https://update.synapse-wireless.com/pypi snapconnect

The files necessary to install *SNAP Connect* will be in the path you specify.  To install from the cache:

.. code-block:: bash

    pip install --no-index --find-links=”/mypathtosave/” snapconnect

.. note:: The *SNAP Connect* E10 comes with *SNAP Connect* pre-installed; however, you will need to reinstall
    *SNAP Connect* if you reinstall the E10's Linux image.

