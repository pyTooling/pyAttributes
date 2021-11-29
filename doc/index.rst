.. include:: shields.inc

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:pyAttributes-github| |SHIELD:svg:pyAttributes-src-license| |SHIELD:svg:pyAttributes-tag| |SHIELD:svg:pyAttributes-release| |SHIELD:svg:pyAttributes-date| |SHIELD:svg:pyAttributes-lib-dep|
   |  |SHIELD:svg:pyAttributes-gha-test| |SHIELD:svg:pyAttributes-codacy-quality| |SHIELD:svg:pyAttributes-codacy-coverage| |SHIELD:svg:pyAttributes-codecov-coverage| |SHIELD:svg:pyAttributes-lib-rank|
   |  |SHIELD:svg:pyAttributes-pypi-tag| |SHIELD:svg:pyAttributes-pypi-status| |SHIELD:svg:pyAttributes-pypi-python| |SHIELD:svg:pyAttributes-lib-status| |SHIELD:svg:pyAttributes-req-status|
   |  |SHIELD:svg:pyAttributes-doc-license| |SHIELD:svg:pyAttributes-ghp-doc|

.. only:: latex

   |SHIELD:png:pyAttributes-github| |SHIELD:png:pyAttributes-src-license| |SHIELD:png:pyAttributes-tag| |SHIELD:png:pyAttributes-release| |SHIELD:png:pyAttributes-date| |SHIELD:png:pyAttributes-lib-dep|
   |SHIELD:png:pyAttributes-gha-test| |SHIELD:png:pyAttributes-codacy-quality| |SHIELD:png:pyAttributes-codacy-coverage| |SHIELD:png:pyAttributes-codecov-coverage| |SHIELD:png:pyAttributes-lib-rank|
   |SHIELD:png:pyAttributes-pypi-tag| |SHIELD:png:pyAttributes-pypi-status| |SHIELD:png:pyAttributes-pypi-python| |SHIELD:png:pyAttributes-lib-status| |SHIELD:png:pyAttributes-req-status|
   |SHIELD:png:pyAttributes-doc-license| |SHIELD:png:pyAttributes-ghp-doc|


pyAttributes Documentation
##########################

The Python package pyAttributes offers implementations of .NET-like attributes
realized with Python decorators. The package also offers a mixin-class to ease
using classes having annotated methods.

In addition, an ArgParseAttributes module is provided, which allows users to
describe complex argparse commond-line argument parser structures in a
declarative way.

Attributes can create a complex class hierarchy. This helps in finding and
filtering for annotated properties and user-defined data. These search
operations can be called globally on the attribute classes or locally within
an annotated class. Therefore the provided helper-mixin should be inherited.

Use Cases
*********

**Annotate properties and user-defined data to methods.**

.. rubric:: Derived use cases:

* Describe a command line argument parser (argparse). |br|
  See `pyAttributes Documentation -> ArgParse Examples <https://pyTooling.GitHub.io/pyAttributes/ArgParse.html>`_
* Mark class members for documentation. |br|
  See `SphinxExtensions <https://sphinxextensions.readthedocs.io/en/latest/>`_ -> DocumentMemberAttribute

.. rubric:: Planned implementations:

* Annotate user-defined data to classes.
* Describe test cases and test suits to get a cleaner syntax for Python's unit
  tests.

Technique
*********

The annotated data is stored in an additional ``__dict__`` entry for each
annotated method. By default the entry is called ``__pyattr__``. Multiple
attributes can be applied to the same method.


Common Attributes
*****************

* :class:`Attribute` class
* :class:`AttributeHelperMixin` class

Special Attributes
******************

This package brings special attribute implementations for:

* Python's :mod:`ArgParse` including sub-parser support.


Contributors
************

* `Patrick Lehmann <https://GitHub.com/Paebbels>`__ (Maintainer)
* `and more... <https://GitHub.com/pyTooling/pyAttributes/graphs/contributors>`__



License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Installation
   Dependencies

.. toctree::
   :caption: Examples
   :hidden:

   ArgParse

.. toctree::
   :caption: Attribute Classes
   :hidden:

   pyAttributes
   pyAttributes.ArgParseAttributes

.. toctree::
   :caption: Appendix
   :hidden:

   Coverage Report ➚ <https://pyTooling.GitHub.io/pyAttributes/coverage/>
   Static Type Check Report ➚ <https://pyTooling.GitHub.io/pyAttributes/typing/>
   License
   Doc-License
   genindex
   py-modindex
