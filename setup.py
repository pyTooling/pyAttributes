# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
#
# =============================================================================
#                 _   _   _        _ _           _
#  _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___
# | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \
# | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|
# |_|    |___/
#
# =============================================================================
# Authors:						Patrick Lehmann
#
# Python package:	    pyAttribute Implementation
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2019 Patrick Lehmann - Bötzingen, Germany
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
# ============================================================================
#
import setuptools

with open("README.md", "r") as file:
	long_description = file.read()

setuptools.setup(
	name="pyAttribute",
	version="0.2.1",
	author="Patrick Lehmann",
	author_email="Paebbels@gmail.com",
	description=".NET-like Attributes implemented as Python decorators.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Paebbels/pyAttribute",
	packages=setuptools.find_packages(),
	classifiers=[
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities"
	],
	python_requires='>=3.5',
)
