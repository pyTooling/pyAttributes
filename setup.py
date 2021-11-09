# =============================================================================
#                  _   _   _        _ _           _
#   _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___  ___
#  | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \/ __|
#  | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/\__ \
#  | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___||___/
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Package installer:  pyAttributes Package Configuration.
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
from pathlib    import Path
from setuptools import (
	setup as setuptools_setup,
	find_namespace_packages as setuptools_find_namespace_packages
)

gitHubNamespace =       "pyTooling"
projectName =           "pyAttributes"
projectNameWithPrefix = projectName
version =               "2.3.0"

# Read README for upload to PyPI
readmeFile = Path("README.md")
with readmeFile.open("r") as file:
	long_description = file.read()

# Read requirements file and add them to package dependency list
requirementsFile = Path("requirements.txt")
with requirementsFile.open("r") as file:
	requirements = [line for line in file.readlines()]

# Derive URLs
sourceCodeURL =     f"https://github.com/{gitHubNamespace}/{projectName}"
documentationURL =  f"https://{gitHubNamespace}.github.io/{projectName}"

# Assemble all package information
setuptools_setup(
	name=projectNameWithPrefix,
	version=version,

	author="Patrick Lehmann",
	author_email="Paebbels@gmail.com",
	# maintainer="Patrick Lehmann",
	# maintainer_email="Paebbels@gmail.com",
  license='Apache 2.0',

	description=".NET-like Attributes implemented as Python decorators.",
	long_description=long_description,
	long_description_content_type="text/markdown",

	url=sourceCodeURL,
	project_urls={
		'Documentation': f"{documentationURL}",
		'Source Code':   f"{sourceCodeURL}",
		'Issue Tracker': f"{sourceCodeURL}/issues"
	},

	packages=setuptools_find_namespace_packages(exclude=["tests", "tests.*",]),
	classifiers=[
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3 :: Only",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Utilities"
	],
	keywords="Python3 Decorators Attributes",

	python_requires='>=3.6',
	install_requires=requirements,
)
