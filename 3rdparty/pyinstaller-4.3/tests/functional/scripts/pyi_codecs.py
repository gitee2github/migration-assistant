# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2005-2021, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

# Encode unicode string into utf8 and then back to unicode strings.
# The original string and the result should be equal.

import codecs


str_a = 'foo bar fóó bář, fěě, ďěž'
str_a_utf8 = codecs.getencoder('utf-8')(str_a)[0]
str_b = codecs.getdecoder('utf-8')(str_a_utf8)[0]

print('codecs working: %s' % (str_a == str_b))
assert str_a == str_b
