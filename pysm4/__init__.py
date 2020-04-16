# -*- coding: utf-8 -*-


"""
    pysm4
    ~~~~~

    pysm4是国密 SM4算法的Python实现， 提供了`encrypt`、 `decrypt`、 `encrypt_ecb`、
    `decrypt_ecb`、 `encrypt_cbc`、 `decrypt_cbc`等函数用于加密解密。

    :copyright: (c) 2017 by yang3yen.
    :license: MIT, see LICENSE for more details.
"""
# modified by Percy
from .sm4 import encrypt, decrypt, encrypt_ecb, \
    decrypt_ecb, encrypt_cbc, decrypt_cbc, get_round_keys, reduction_mk


__title__ = 'pysm4'
__version__ = '0.7'
__author__ = 'yang3yen'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 yang3yen'
__email__ = 'yang3yen@gmail.com'
