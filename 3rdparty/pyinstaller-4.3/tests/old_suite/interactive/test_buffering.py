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


import sys


print("""test_buffering - unbufferred
  type: 123456<enter>
    should see: 12345
  type: <enter>
    if unbuffered should see: 6
    if NOT unbuffered, should see nothing
  type: Q to quit

input:""")
# Ensure the previous message is fully printed to terminal.
sys.stdout.flush()


while True:
    data = sys.stdin.read(5)
    sys.stdout.write(data)
    sys.stdout.flush()
    if 'Q' in data or 'q' in data:
        break


print('test_buffering - done')
