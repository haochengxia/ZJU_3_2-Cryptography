from sys import version_info
import math
from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify

__all__ = ['encrypt', 'decrypt','list_all_ed']

if version_info[0] == 2:
    # python2
    PY2 = True
    PY3 = False
else:
    # python3
    PY2 = False
    PY3 = True

E_FMT = 'UTF8'



def encrypt(plain_num, e, n):
    """
    rsa encrypt 加密
    输入明文和私钥
    """
    return _crypt(plain_num, e ,n)


def decrypt(cipher_num, d ,n):
    """
    rsa decrypt 解密
    输入密文和公钥
    """
    return _crypt(cipher_num, d ,n)


def gen_d(p , q, e):
    m = _euler(p, q)
    d = _module_reverse(e, m)
    return d


def list_all_ed(p, q):
    ed_list = []
    m = _euler(p, q)
    for i in range(2, m):
        if _check_relatively_prime(i, m):
            e = i
            d = _module_reverse(e, m)
            ed = [e,d]
            ed_list.append(ed)
    return ed_list


def _euler(p, q):
    _euler_n = (p - 1) * (q - 1)
    return _euler_n


def _check_relatively_prime(a, b):
    """
    使用辗转相除法确定最大公约数，进行互质判断
    """
    if _gcd(a, b) == 1:
        return True
    else:
        return False


def _crypt(num, k ,n):
    _res = pow(num, k) % n
    return _res


def _gcd(a, b):
    """
    辗转相除法返回最大公约数
    """
    if a > b:
        a = a + b
        b = a - b
        a = a - b
    _res = a % b
    while _res != 0:
        a = b
        b = _res
        _res = a % b
    return b


def _module_reverse(e, m):
    """
    取模反 (e*d) = 1 mod Euler(n)
    """
    _mod_rev = 0
    for i in range(2, m):
        if (i * e) % m == 1:
            _mod_rev = i
    return _mod_rev
