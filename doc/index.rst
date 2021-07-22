.. |img-pyAttributes-github| image:: https://img.shields.io/badge/Paebbels-pyAttributes-323131.svg?logo=github&longCache=true
   :alt: Sourcecode on GitHub
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes
.. |img-pyAttributes-codelicense| image:: https://img.shields.io/pypi/l/pyAttributes?logo=GitHub&label=code%20license
   :alt: Sourcecode License
   :height: 22
.. |img-pyAttributes-tag| image:: https://img.shields.io/github/v/tag/Paebbels/pyAttributes?logo=GitHub&include_prereleases
   :alt: GitHub tag (latest SemVer incl. pre-release)
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
.. |img-pyAttributes-lib-dep| image:: https://img.shields.io/librariesio/dependents/pypi/pyAttributes?logo=librariesdotio
   :alt: Dependents (via libraries.io)
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes/network/dependents
.. |img-pyAttributes-gha-pipeline| image:: https://img.shields.io/github/workflow/status/Paebbels/pyAttributes/Unit%20Testing,%20Coverage%20Collection,%20Package,%20Release,%20Documentation%20and%20Publish?label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF
   :alt: GitHub Workflow - Build and Test Status
   :height: 22
   :target: https://github.com/Paebbels/pyAttributes/actions/workflows/Pipeline.yml
.. |img-pyAttributes-codacy-quality| image:: https://img.shields.io/codacy/grade/b63aac7ef7e34baf829f11a61574bbaf?logo=Codacy
   :alt: Codacy - Quality
   :height: 22
   :target: https://www.codacy.com/manual/Paebbels/pyAttributes
.. |img-pyAttributes-codacy-coverage| image:: https://img.shields.io/codacy/coverage/b63aac7ef7e34baf829f11a61574bbaf?logo=Codacy
   :alt: Codacy - Line Coverage
   :height: 22
   :target: https://www.codacy.com/manual/Paebbels/pyAttributes
.. |img-pyAttributes-codecov-coverage| image:: https://img.shields.io/codecov/c/github/Paebbels/pyAttributes?logo=Codecov
   :alt: Codecov - Branch Coverage
   :height: 22
   :target: https://codecov.io/gh/Paebbels/pyAttributes
.. |img-pyAttributes-lib-rank| image:: https://img.shields.io/librariesio/sourcerank/pypi/pyAttributes?logo=librariesdotio
   :alt: Libraries.io SourceRank
   :height: 22
   :target: https://libraries.io/github/Paebbels/pyAttributes/sourcerank
.. |img-pyAttributes-pypi-tag| image:: https://img.shields.io/pypi/v/pyAttributes?logo=PyPI&logoColor=FBE072
   :alt: PyPI - Tag
   :height: 22
   :target: https://pypi.org/project/pyAttributes/
.. |img-pyAttributes-pypi-python| image:: https://img.shields.io/pypi/pyversions/pyAttributes?logo=PyPI&logoColor=FBE072
   :alt: PyPI - Python Version
   :height: 22
.. |img-pyAttributes-pypi-status| image:: https://img.shields.io/pypi/status/pyAttributes?logo=PyPI&logoColor=FBE072
   :alt: PyPI - Status
   :height: 22
.. |img-pyAttributes-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pyAttributes?logo=librariesdotio
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/Paebbels/pyAttributes
.. |img-pyAttributes-req-status| image:: https://img.shields.io/requires/github/Paebbels/pyAttributes
   :alt: Requires.io
   :height: 22
   :target: https://requires.io/github/Paebbels/pyAttributes/requirements/?branch=master
.. |img-pyAttributes-rtd| image:: https://img.shields.io/readthedocs/pyattributes?label=ReadTheDocs&logo=readthedocs
   :alt: Read the Docs
   :height: 22
   :target: https://pyAttributes.readthedocs.io/
.. |img-pyAttributes-doclicense| image:: https://img.shields.io/badge/doc%20license-CC--BY%204.0-green?logo=readthedocs
   :alt: Documentation License
   :height: 22
   :target: LICENSE.md
.. |img-pyAttributes-doc| image:: https://img.shields.io/badge/doc-read%20now%20%E2%9E%94-blueviolet?logo=readthedocs
   :alt: Documentation - Read Now!
   :height: 22
   :target: https://pyAttributes.readthedocs.io/

|img-pyAttributes-github| |img-pyAttributes-codelicense| |img-pyAttributes-tag| |img-pyAttributes-release| |img-pyAttributes-date| |img-pyAttributes-lib-dep| |br|
|img-pyAttributes-gha-pipeline| |img-pyAttributes-codacy-quality| |img-pyAttributes-codacy-coverage| |img-pyAttributes-codecov-coverage| |img-pyAttributes-lib-rank| |br|
|img-pyAttributes-pypi-tag| |img-pyAttributes-pypi-python| |img-pyAttributes-pypi-status| |img-pyAttributes-lib-status| |img-pyAttributes-req-status| |br|
|img-pyAttributes-rtd| |img-pyAttributes-doclicense| |img-pyAttributes-doc|

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

* `Patrick Lehmann <https://github.com/Paebbels>`__ (Maintainer)
* `and more... <https://github.com/paebbels/pyCallBy/graphs/contributors>`__


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
