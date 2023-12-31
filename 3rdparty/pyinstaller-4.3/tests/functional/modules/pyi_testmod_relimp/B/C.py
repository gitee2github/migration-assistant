#-----------------------------------------------------------------------------
# Copyright (c) 2013-2021, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------


name = 'pyi_testmod_relimp.B.C'

from . import D                 # Imports pyi_testmod_relimp.B.D
from .D import X                # Imports pyi_testmod_relimp.B.D.X
from .. import E                # Imports pyi_testmod_relimp.E
from ..F import G               # Imports pyi_testmod_relimp.F.G
from ..F import H               # Imports pyi_testmod_relimp.F.H

assert D.name == 'pyi_testmod_relimp.B.D'
assert E.name == 'pyi_testmod_relimp.E'
assert G.name == 'pyi_testmod_relimp.F.G'
assert H.name == 'pyi_testmod_relimp.F.H'
