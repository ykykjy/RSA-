import random

# 小素数表
SmallPrimes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]


def miller_rabin(p):
    """
    Miller-Rabin 算法，检测一个数是不是素数
    :param p: 待检测的数
    :return: 是素数返回true，不是则返回false
    """
    if p % 2 == 0:  # 判断待测试的数p是否是偶数。如果是，那么p不是素数，直接返回false。
        return False
    # p - 1 = (2 ^ k) * t 将p-1分解为2^k * t的形式，其中t是奇数。
    t = p - 1
    k = 0
    while t % 2 == 0:
        t = t // 2
        k += 1

    # 设定一个测试次数k，根据需要选择一个合适的值。k越大，误判率越小，但是算法的时间复杂度也越高。这里选择20次。
    for _ in range(20):
        a = random.randrange(2, p - 1)  # 随机生成一个a，满足1 < a < p-1
        temp1 = pow(a, t, p)  # 计算：temp1 = a^t mod p
        if temp1 != 1:  # 如果temp1等于1，或者temp1等于n-1，那么继续下一次测试
            temp2 = temp1
            for i in range(k):
                temp2 = (temp1 ** 2) % p  # temp1 = temp1^2 mod n。
                # 二次探测
                if temp2 == 1 and temp1 != 1 and temp1 != p - 1:
                    return False
                temp1 = temp2
            # 最终检测
            if temp2 != 1:
                return False
    return True


def is_prime(num):
    """
    判断参数num是不是素数
    :param num: 要判断是否为素数的参数
    :return: true是素数，false不是素数
    """
    if num < 2:  # 0和1不是素数
        return False
    if num in SmallPrimes:  # 小素数, 返回 true
        return True

    return miller_rabin(num)  # Miller-Rabin 算法进一步检测


def get_prime(bitlen):
    """
    随机生成一个二进制有bitlen长度的素数
    :param bitlen: 生成的随机数转换成二进制后的位数
    :return: bitlen长度的素数
    """
    while True:
        num = random.randrange(2 ** (bitlen - 1), 2 ** bitlen)  # 从2**(bitlen-1)到2**bitlen取一随机数
        if is_prime(num):  # 如果num是素数就返回
            return num

# def is_prime(num):  # 最简单的素数判断方法，太慢了
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         sqr = int(math.sqrt(num))
#         for i in range(3, sqr+1, 2):
#             if num % i == 0:
#                 return False
#         return True
