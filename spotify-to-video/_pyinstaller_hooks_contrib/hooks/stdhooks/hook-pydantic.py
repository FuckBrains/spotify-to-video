# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import get_module_attribute, collect_submodules

# By default, pydantic from PyPi comes with all modules compiled as
# cpython extensions, which seems to prevent pyinstaller from automatically
# picking up the submodules
is_compiled = get_module_attribute('pydantic', 'compiled') == 'True'
if is_compiled:
    # Compiled version; we need to manually collect the submodules from
    # pydantic...
    hiddenimports = collect_submodules('pydantic')
    # ... as well as the following modules from the standard library
    hiddenimports += [
        'colorsys',
        'decimal',
        'json',
        'ipaddress',
        'pathlib',
        'uuid',
    ]
