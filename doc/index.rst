.. |img-pyAttributes-github| image:: https://img.shields.io/badge/Paebbels-pyAttributes-323131.svg?logo=github&longCache=true
   :alt: Sourcecode on GitHub
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes
.. |img-pyAttributes-license| image:: https://img.shields.io/badge/Apache%20License,%202.0-bd0000.svg?longCache=true&label=license&logo=Apache&logoColor=D22128
   :alt: License
   :height: 22
.. |img-pyAttributes-tag| image:: https://img.shields.io/github/v/tag/Paebbels/pyAttributes?logo=GitHub&include_prereleases
   :alt: GitHub tag (latest SemVer incl. pre-release
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes/tags
.. |img-pyAttributes-release| image:: https://img.shields.io/github/v/release/Paebbels/pyAttributes?logo=GitHub&include_prereleases
   :alt: GitHub release (latest SemVer incl. including pre-releases
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes/releases/latest
.. |img-pyAttributes-date| image:: https://img.shields.io/github/release-date/Paebbels/pyAttributes?logo=GitHub
   :alt: GitHub release date
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes/releases
.. |img-pyAttributes-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pyAttributes
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/Paebbels/pyAttributes
.. |img-pyAttributes-req-status| image:: https://img.shields.io/requires/github/Paebbels/pyAttributes
   :alt: Requires.io
   :height: 22
   :target: https://requires.io/github/Paebbels/pyAttributes/requirements/?branch=master
.. |img-pyAttributes-travis| image:: https://img.shields.io/travis/com/Paebbels/pyAttributes?logo=Travis
   :alt: Travis - Build on 'master'
   :height: 22
   :target: https://travis-ci.com/Paebbels/pyAttributes
.. |img-pyAttributes-pypi-tag| image:: https://img.shields.io/pypi/v/pyAttributes?logo=PyPI
   :alt: PyPI - Tag
   :height: 22
   :target: https://pypi.org/project/pyAttributes/
.. |img-pyAttributes-pypi-status| image:: https://img.shields.io/pypi/status/pyAttributes?logo=PyPI
   :alt: PyPI - Status
   :height: 22
.. |img-pyAttributes-pypi-python| image:: https://img.shields.io/pypi/pyversions/pyAttributes?logo=PyPI
   :alt: PyPI - Python Version
   :height: 22
.. |img-pyAttributes-lib-dep| image:: https://img.shields.io/librariesio/dependent-repos/pypi/pyAttributes
   :alt: Dependent repos (via libraries.io)
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes/network/dependents
.. |img-pyAttributes-codacy-quality| image:: https://img.shields.io/codacy/grade/b63aac7ef7e34baf829f11a61574bbaf?logo=codacy
   :alt: Codacy - Quality
   :height: 22
   :target: https://www.codacy.com/manual/Paebbels/pyAttributes
.. |img-pyAttributes-codacy-coverage| image:: https://img.shields.io/codacy/coverage/b63aac7ef7e34baf829f11a61574bbaf?logo=codacy
   :alt: Codacy - Line Coverage
   :height: 22
   :target: https://www.codacy.com/manual/Paebbels/pyAttributes
.. |img-pyAttributes-codecov-coverage| image:: https://codecov.io/gh/Paebbels/pyAttributes/branch/master/graph/badge.svg
   :alt: Codecov - Branch Coverage
   :height: 22
   :target: https://codecov.io/gh/Paebbels/pyAttributes
.. |img-pyAttributes-lib-rank| image:: https://img.shields.io/librariesio/sourcerank/pypi/pyAttributes
   :alt: Libraries.io SourceRank
   :height: 22
   :target: https://libraries.io/github/Paebbels/pyAttributes/sourcerank
.. |img-pyAttributes-rtd| image:: https://img.shields.io/readthedocs/pyattributes
   :alt: Read the Docs
   :height: 22
   :target: https://pyAttributes.readthedocs.io/en/latest/

|img-pyAttributes-github| |img-pyAttributes-tag| |img-pyAttributes-release| |img-pyAttributes-date| |br|
|img-pyAttributes-lib-status| |img-pyAttributes-req-status| |img-pyAttributes-lib-dep| |br|
|img-pyAttributes-travis| |img-pyAttributes-pypi-tag| |img-pyAttributes-pypi-status| |img-pyAttributes-pypi-python| |br|
|img-pyAttributes-codacy-quality| |img-pyAttributes-codacy-coverage| |img-pyAttributes-codecov-coverage| |img-pyAttributes-lib-rank| |br|
|img-pyAttributes-rtd| |img-pyAttributes-license|

.. code-block::

                     _   _   _        _ _           _
      _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___  ___
     | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \/ __|
     | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/\__ \
     | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___||___/
     |_|    |___/

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

.. topic:: Derived use cases:

* Describe a command line argument parser (argparse). |br|
  See `pyAttributes Documentation -> ArgParse Examples <https://pyattributes.readthedocs.io/en/latest/ArgParse.html>`_
* Mark class members for documentation. |br|
  See `SphinxExtensions <https://sphinxextensions.readthedocs.io/en/latest/>`_ -> DocumentMemberAttribute

.. topic:: Planned implementations:

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

* `Patrick Lehmann <https://github.com/Paebbels>`_ (Maintainer)



License
*******

This library is licensed under **Apache License 2.0**.

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

   License
   genindex
   py-modindex
