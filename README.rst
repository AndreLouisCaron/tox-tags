tox-tags
========

This is a Tox_ plug-in that allows you to tag test environments and then easily
select a subset of test environments when running Tox.

The plug-in and its rule system is heavily inspired by `nose-attrib`_.

Here's an example::

    [tox]
    envlist =
      py27-win,
      py27,
      py34,

    [testenv:py27-win]
    tags =
      win

Then, you can easily run only the ``py27-win`` environment::

    $ tox -t win

You can also run all but the ``py27-win`` environment::

    $ tox -t '!win'

.. _Tox: https://tox.readthedocs.org/en/latest/
.. _`nose-attrib`: http://nose.readthedocs.org/en/latest/plugins/attrib.html
