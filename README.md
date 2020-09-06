[![Sourcecode on GitHub](https://img.shields.io/badge/Paebbels-pyAttributes-323131.svg?logo=github&longCache=true)](https://github.com/Paebbels/pyAttributes)
[![License](https://img.shields.io/badge/Apache%20License,%202.0-bd0000.svg?longCache=true&label=code%20license&logo=Apache&logoColor=D22128)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/Paebbels/pyAttributes?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyAttributes/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/Paebbels/pyAttributes?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyAttributes/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/Paebbels/pyAttributes?logo=GitHub&)](https://github.com/Paebbels/pyAttributes/releases)  
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Paebbels/pyAttributes/Test,%20Coverage%20and%20Release?label=Workflow&logo=GitHub)](https://github.com/Paebbels/pyAttributes/actions?query=workflow%3A%22Test%2C+Coverage+and+Release%22)
[![PyPI](https://img.shields.io/pypi/v/pyAttributes?logo=PyPI)](https://pypi.org/project/pyAttributes/)
![PyPI - Status](https://img.shields.io/pypi/status/pyAttributes?logo=PyPI)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyAttributes?logo=PyPI)
[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyAttributes)](https://github.com/Paebbels/pyAttributes/network/dependents)  
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyAttributes)](https://libraries.io/github/Paebbels/pyAttributes)
[![Requires.io](https://img.shields.io/requires/github/Paebbels/pyAttributes)](https://requires.io/github/Paebbels/pyAttributes/requirements/?branch=master)  
[![Codacy - Quality](https://api.codacy.com/project/badge/Grade/b63aac7ef7e34baf829f11a61574bbaf)](https://www.codacy.com/manual/Paebbels/pyAttributes)
[![Codacy - Coverage](https://api.codacy.com/project/badge/Coverage/b63aac7ef7e34baf829f11a61574bbaf)](https://www.codacy.com/manual/Paebbels/pyAttributes)
[![Codecov - Branch Coverage](https://codecov.io/gh/Paebbels/pyAttributes/branch/master/graph/badge.svg)](https://codecov.io/gh/Paebbels/pyAttributes)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyAttributes)](https://libraries.io/github/Paebbels/pyAttributes/sourcerank)  
[![Read the Docs](https://img.shields.io/readthedocs/pyattributes)](https://pyAttributes.readthedocs.io/en/latest/)

# pyAttributes

The Python package `pyAttributes` offers implementations of .NET-like attributes
realized with Python decorators. The package also offers a mixin-class to ease
using classes having annotated methods.

In addition, an `ArgParseAttributes` module is provided, which allows users to
describe complex argparse commond-line argument parser structures in a declarative
way.

Attributes can create a complex class hierarchy. This helps in finding and
filtering for annotated properties and user-defined data. These search operations
can be called globally on the attribute classes or locally within an annotated
class. Therefore the provided helper-mixin should be inherited.


## Use Cases

***Annotate properties and user-defined data to methods.***

**Derived use cases:**
* Describe a command line argument parser (argparse).  
  See [pyAttributes Documentation -> ArgParse Examples](https://pyattributes.readthedocs.io/en/latest/ArgParse.html)
* Mark class members for documentation.  
  See [SphinxExtensions](https://sphinxextensions.readthedocs.io/en/latest/) -> DocumentMemberAttribute

**Planned implementations:**
* Annotate user-defined data to classes.
* Describe test cases and test suits to get a cleaner syntax for Python's unit tests.


## Technique

The annotated data is stored in an additional ``__dict__`` entry for each
annotated method. By default the entry is called ``__pyattr__``. Multiple
attributes can be applied to the same method.



## Creating new Attributes
### Simple User-Defined Attribute

```python
class SimpleAttribute(Attribute):
  pass
```

### User-Defined Attribute with Data

```python
class DataAttribute(Attribute):
  data: str = None

  def __init__(self, data:str):
    self.data = data

  @property
  def Data(self):
    return self.data
```


## Applying Attributes to Methods

```python
class ProgramWithHelper(AttributeHelperMixin):
  @SimpleAttribute()
  def Method_1(self):
    """This method is marked as simple."""

  @DataAttribute("hello world")
  def Method_2(self):
    """This method as annotated data."""
```

## Finding Methods with Attributes
### Finding Methods with Global Search

```python
methods = SimpleAttribute.GetMethods()
for method, attributes in methods.items():
  print(method)
  for attribute in attributes:
    print("  ", attribute)
```

### Finding Methods with Class-Wide Search

```python
class ProgramWithHelper(AttributeHelperMixin):
  @SimpleAttribute()
  def Method_1(self):
    """This method is marked as simple."""

  @DataAttribute("hello world")
  def Method_2(self):
    """This method as annotated data."""
 
  def test_GetMethods(self):
    methods = self.GetMethods(filter=DataAttribute)
    for method, attributes in methods.items():
      print(method)
      for attribute in attributes:
        print("  ", attribute)

  def test_GetAttributes(self):
    attributes = self.GetAttributes(self.Method_1)
    for attribute in attributes:
      print("  ", attribute)
```


## Contributors

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)


## License

This library is licensed under [Apache License 2.0](LICENSE.md)

-------------------------

SPDX-License-Identifier: Apache-2.0
