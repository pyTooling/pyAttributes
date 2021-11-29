[![Sourcecode on GitHub](https://img.shields.io/badge/pyTooling-pyAttributes-323131.svg?logo=github&longCache=true)](https://GitHub.com/pyTooling/pyAttributes)
[![Sourcecode License](https://img.shields.io/pypi/l/pyAttributes?logo=GitHub&label=code%20license)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/pyTooling/pyAttributes?logo=GitHub&include_prereleases)](https://GitHub.com/pyTooling/pyAttributes/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/pyTooling/pyAttributes?logo=GitHub&include_prereleases)](https://GitHub.com/pyTooling/pyAttributes/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/pyTooling/pyAttributes?logo=GitHub)](https://GitHub.com/pyTooling/pyAttributes/releases)
[![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/pyAttributes?logo=librariesdotio)](https://GitHub.com/pyTooling/pyAttributes/network/dependents)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/pyTooling/pyAttributes/Unit%20Testing,%20Coverage%20Collection,%20Package,%20Release,%20Documentation%20and%20Publish?label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/pyTooling/pyAttributes/actions/workflows/Pipeline.yml)
[![Codacy - Quality](https://img.shields.io/codacy/grade/b63aac7ef7e34baf829f11a61574bbaf?logo=Codacy)](https://www.codacy.com/manual/pyTooling/pyAttributes)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/b63aac7ef7e34baf829f11a61574bbaf?logo=Codacy)](https://www.codacy.com/manual/pyTooling/pyAttributes)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/pyTooling/pyAttributes?logo=Codecov)](https://codecov.io/gh/pyTooling/pyAttributes)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyAttributes?logo=librariesdotio)](https://libraries.io/github/pyTooling/pyAttributes/sourcerank)  
[![PyPI](https://img.shields.io/pypi/v/pyAttributes?logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyAttributes/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyAttributes?logo=PyPI&logoColor=FBE072)
![PyPI - Status](https://img.shields.io/pypi/status/pyAttributes?logo=PyPI&logoColor=FBE072)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyAttributes?logo=librariesdotio)](https://libraries.io/github/pyTooling/pyAttributes)
[![Requires.io](https://img.shields.io/requires/github/pyTooling/pyAttributes)](https://requires.io/github/pyTooling/pyAttributes/requirements/?branch=main)  
[![Documentation License](https://img.shields.io/badge/doc%20license-CC--BY%204.0-green?logo=readthedocs)](doc/Doc-License.rst)
[![Documentation - Read Now!](https://img.shields.io/badge/doc-read%20now%20%E2%9E%9A-blueviolet?logo=readthedocs)](https://pyTooling.GitHub.io/pyAttributes)

# pyAttributes

The Python package `pyAttributes` offers implementations of .NET-like attributes
realized with Python decorators. The package also offers a mixin-class to ease
using classes having annotated methods.

In addition, an `ArgParseAttributes` module is provided, which allows users to
describe complex argparse command-line argument parser structures in a declarative
way.

Attributes can create a complex class hierarchy. This helps in finding and
filtering for annotated properties and user-defined data. These search operations
can be called globally on the attribute classes or locally within an annotated
class. Therefore the provided helper-mixin should be inherited.


## Use Cases

***Annotate properties and user-defined data to methods.***

**Derived use cases:**
* Describe a command line argument parser (argparse).  
  See [pyAttributes Documentation -> ArgParse Examples](https://pyTooling.GitHub.io/pyAttributes/ArgParse.html)
* Mark class members for documentation.  
  See [SphinxExtensions](https://sphinxextensions.readthedocs.io/en/latest/) -> DocumentMemberAttribute

**Planned implementations:**
* Annotate user-defined data to classes.
* Describe test cases and test suits to get a cleaner syntax for Python's unit tests.


## Technique

The annotated data is stored in an additional ``__dict__`` entry for each
annotated method. By default, the entry is called ``__pyattr__``. Multiple
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

* [Patrick Lehmann](https://GitHub.com/Paebbels) (Maintainer)
* [and more...](https://GitHub.com/pyTooling/pyAttributes/graphs/contributors) 


## License

This Python package (source code) licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).


-------------------------

SPDX-License-Identifier: Apache-2.0
