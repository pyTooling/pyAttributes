# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
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
# Python unittest:    Helper functions for unittests
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2020 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
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
"""
pyAttributes
############

:copyright: Copyright 2007-2020 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""

from typing       import Generator, Dict, TypeVar, Tuple

K1 = TypeVar("K1")
V1 = TypeVar("V1")
K2 = TypeVar("K2")
V2 = TypeVar("V2")

def zip(dict1: Dict[K1, V1], dict2: Dict[K2, V2]) -> Generator[Tuple[K1, K2, V1, V2], None, None]:
	l1 = len(dict1)
	l2 = len(dict2)

	if (l1 != l2):
		if (l1 < l2):
			raise ValueError("'dict1' (len={}) has less elements than 'dict2' (len={}).".format(l1, l2))
		else:
			raise ValueError("'dict1' (len={}) has more elements than 'dict2' (len={}).".format(l1, l2))

	iter1 = iter(dict1.items())
	iter2 = iter(dict2.items())

	try:
		while True:
			key1, value1 = next(iter1)
			key2, value2 = next(iter2)

			yield (key1, key2, value1, value2)

	except StopIteration:
		return
