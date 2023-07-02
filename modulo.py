def gcd(a, b):
    """
    欧几里得算法求a和b的最大公约数
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ext_gcd(a, b):
    """
    扩展欧几里得算法求a和b的最大公约数，返回gcd(a, b)、x和y
    gcd: a和b的最大公约数
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = ext_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


def mod_inverse(a, m):
    gcd, x, _ = ext_gcd(a, m)
    if gcd != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def mont_red(x, r, k, n):
    """
    蒙哥马利约减
    计算 X / R mod N (R = 2 ^ k 且 R > N 且 R 和 N 互素)
    """
    assert (r == 1 << k)
    gcd, inv_r, inv_n = ext_gcd(r, n)
    assert (gcd == 1)
    m = x * (-inv_n) % r
    y = (x + m * n) >> k
    return (y - n) if (y > n) else y


def mont_mul(a, b, n):
    """
    蒙哥马利模乘
    计算 a * b mod n
    """
    k = n.bit_length()
    r = 1 << k
    a_dot = a * r % n
    b_dot = b * r % n
    x = a_dot * b_dot
    x1 = mont_red(x, r, k, n)
    y = mont_red(x1, r, k, n)
    return y


def chinese_remainder_theorem(a, m):
    """
    中国剩余定理
    """
    M = 1
    for mi in m:
        M *= mi
    x = 0
    for ai, mi in zip(a, m):
        Mi = M // mi
        xi = mod_inverse(Mi, mi)
        x += ai * xi * Mi
    return x % M


def rep_quad_mod_pow(x, k, n):
    """
    计算 x ^ k mod n(模重复平方法)
    """
    a = 1
    b = x
    bit_array = bin(k)[2:][::-1]
    for i in bit_array:
        if i == '1':
            a = a * b % n
        b = b * b % n
    return a


def mont_pow(x, k, n):
    """
    蒙哥马利模幂（蒙哥马利算法）
    计算 x ^ k mod n
    """
    a = 1
    b = x
    bit_array = bin(k)[2:][::-1]
    for i in bit_array:
        if i == '1':
            a = mont_mul(a, b, n)
        b = mont_mul(b, b, n)
    return a


def power_modulo(x, k, n):
    """
    中国剩余定理求 x^k mod n
    """
    a = []
    m = []
    for p in range(2, n + 1):
        if n % p == 0:
            q = 1
            while n % (p ** q) == 0:
                q += 1
            q -= 1
            m.append(p ** q)
            a.append(x ** (k % (p ** q)) % (p ** q))
    return chinese_remainder_theorem(a, m)


