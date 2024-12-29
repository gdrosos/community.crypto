# -*- coding: utf-8 -*-

# Copyright (c) 2022, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r"""
requirements:
  - cryptography >= 1.2.3 (older versions might work as well)
attributes:
  diff_mode:
    support: none
options:
  src_path:
    description:
      - Name of the file containing the OpenSSL private key to convert.
      - Exactly one of O(src_path) or O(src_content) must be specified.
    type: path
  src_content:
    description:
      - The content of the file containing the OpenSSL private key to convert.
      - Exactly one of O(src_path) or O(src_content) must be specified.
    type: str
  src_passphrase:
    description:
      - The passphrase for the private key to load.
    type: str
  dest_passphrase:
    description:
      - The passphrase for the private key to store.
    type: str
  format:
    description:
      - Determines which format the destination private key should be written in.
      - Please note that not every key can be exported in any format, and that not every format supports encryption.
    type: str
    choices: [pkcs1, pkcs8, raw]
    required: true
seealso:
  - module: community.crypto.openssl_privatekey
  - module: community.crypto.openssl_privatekey_pipe
  - module: community.crypto.openssl_publickey
"""
