[![Sourcecode on GitHub](https://img.shields.io/badge/Paebbels-pyAttributes-323131.svg?logo=github&longCache=true)](https://github.com/Paebbels/pyAttributes)
[![Sourcecode License](https://img.shields.io/pypi/l/pyAttributes?logo=GitHub&label=code%20license)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/Paebbels/pyAttributes?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyAttributes/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/Paebbels/pyAttributes?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyAttributes/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/Paebbels/pyAttributes?logo=GitHub)](https://github.com/Paebbels/pyAttributes/releases)
[![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/pyAttributes?logo=librariesdotio)](https://github.com/Paebbels/pyAttributes/network/dependents)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/Paebbels/pyAttributes/Unit%20Testing,%20Coverage%20Collection,%20Package,%20Release,%20Documentation%20and%20Publish?label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF)](https://github.com/Paebbels/pyAttributes/actions/workflows/Pipeline.yml)
[![Codacy - Quality](https://img.shields.io/codacy/grade/b63aac7ef7e34baf829f11a61574bbaf?logo=Codacy)](https://www.codacy.com/manual/Paebbels/pyAttributes)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/b63aac7ef7e34baf829f11a61574bbaf?logo=Codacy)](https://www.codacy.com/manual/Paebbels/pyAttributes)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/Paebbels/pyAttributes?logo=Codecov)](https://codecov.io/gh/Paebbels/pyAttributes)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyAttributes?logo=librariesdotio)](https://libraries.io/github/Paebbels/pyAttributes/sourcerank)  
[![PyPI](https://img.shields.io/pypi/v/pyAttributes?logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyAttributes/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyAttributes?logo=PyPI&logoColor=FBE072)
![PyPI - Status](https://img.shields.io/pypi/status/pyAttributes?logo=PyPI&logoColor=FBE072)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyAttributes?logo=librariesdotio)](https://libraries.io/github/Paebbels/pyAttributes)
[![Requires.io](https://img.shields.io/requires/github/Paebbels/pyAttributes)](https://requires.io/github/Paebbels/pyAttributes/requirements/?branch=main)  
[![Read the Docs](https://img.shields.io/readthedocs/pyattributes?label=ReadTheDocs&logo=readthedocs)](https://pyAttributes.readthedocs.io/)
[![Documentation License](https://img.shields.io/badge/doc%20license-CC--BY%204.0-green?logo=readthedocs)](LICENSE.md)
[![Documentation - Read Now!](https://img.shields.io/badge/doc-read%20now%20%E2%9E%9A-blueviolet?logo=readthedocs)](https://pyAttributes.readthedocs.io/)

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
  See [pyAttributes Documentation -> ArgParse Examples](https://pyattributes.readthedocs.io/en/latest/ArgParse.html)
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

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)
* [and more...](https://github.com/Paebbels/pyAttributes/graphs/contributors) 


## License

This Python package (source code) licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).


-------------------------

SPDX-License-Identifier: Apache-2.0
