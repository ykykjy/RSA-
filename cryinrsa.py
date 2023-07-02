import time
from prime import *
from modulo import *
from file import *


def gen_key(bitlen):
    """
    生成一组密钥, 并存放到文件当中
    :param bitlen: 生成密钥时p和q的长度
    """
    p = get_prime(bitlen)  # p是bitlen长度的素数
    q = get_prime(bitlen)  # q是bitlen长度的素数
    while q == p:  # 其中p不等于q，否则重新生成素数
        q = get_prime(bitlen)
    n = p * q  # 生成一个大素数，使得n等于p*q
    n_len = n.bit_length()
    if n_len % 8 == 0:
        block = n_len // 8
    else:
        block = n_len // 8 + 1
    fn = (p - 1) * (q - 1)
    d = 0  # 找到e,d使得ed + xfn = 1
    e = 0
    while d == 0:
        e = random.randrange(2, fn)
        g, d, _ = ext_gcd(e, fn)
        if g != 1:
            d = 0
    d = d % fn

    pub_data = str(e) + ' ' + str(n) + ' ' + str(block)
    pri_data = str(d) + ' ' + str(n) + ' ' + str(block)
    write_data('./key/publicKey/pub.txt', pub_data, 'w+')
    write_data('./key/privateKey/pri.txt', pri_data, 'w+')
    # with open('./key/publicKey/pub.txt', 'w+') as fp:  # 共私钥进行存储
    #     fp.write(str(e) + ' ' + str(n) + ' ' + str(block))
    # with open('./key/privateKey/pri.txt', 'w+') as fp:
    #     fp.write(str(d) + ' ' + str(n) + ' ' + str(block))


def encrypt(in_file, out_file, public_key):
    """
    对文件中的字节进行加密
    :param in_file: 要加密的文件路径
    :param out_file: 加密后字节存放的文件路径
    """
    enblock = read_data(public_key, 'r')
    e, n, block = enblock.split()
    e = int(e)
    n = int(n)
    block = int(block)
    cipher_bytes = bytes()
    plain_bytes = read_data(in_file, 'rb')
    length = len(plain_bytes)
    for i in range(0, length, block):
        j = (i + block) if (i + block < length) else length
        m = int.from_bytes(plain_bytes[i:j], 'big')  # 将当前块的明文转换为整数，'big' 参数表示使用大端字节序。
        # c = pow(m, e, n)  # 0.0010001659393310547
        c = rep_quad_mod_pow(m, e, n)  # 模重复平方法  0.0010006427764892578
        # c = mont_pow(m, e, n)  # 蒙哥马利算法  0.009002208709716797
        # c = power_modulo(m, e, n)
        # 将加密结果转换为 bytes 数组，并添加到密文字节数组中，'big' 参数表示使用大端字节序。
        cipher_bytes += c.to_bytes(block, 'big')
    write_data(out_file, cipher_bytes, 'wb')


# 解密, 按 block 字节读, 缩减为 block - 1 字节存
def decrypt(in_file, out_file, private_key):
    """
    对文件中的字节进行解密
    :param in_file: 要解密的文件路径
    :param out_file: 解密后字节存放的文件路径
    """
    enblock = read_data(private_key, 'r')
    d, n, block = enblock.split()
    d = int(d)
    n = int(n)
    block = int(block)
    plain_bytes = bytes()
    cipher_bytes = read_data(in_file, 'rb')
    length = len(cipher_bytes)
    for i in range(0, length, block):
        j = (i + block) if (i + block < length) else length
        c = int.from_bytes(cipher_bytes[i:j], 'big')
        # m = pow(c, d, n)
        start_time = time.perf_counter()
        # m = rep_quad_mod_pow(c, d, n)  # 模重复平方法
        # m = mont_pow(c, d, n)  # 蒙哥马利算法
        # m = power_modulo(c, d, n)  # 中国剩余定理
        m = pow(c, d, n)
        end_time = time.perf_counter()
        print("取模运算所用的时间：{:.10f}秒".format(end_time - start_time))
        m = m.to_bytes(block, 'big')
        if j == length:
            k = 0
            for i in range(block):
                if m[i:i + 1] == b'\x00':
                    k += 1
                else:
                    break
            m = m[k:j]
        plain_bytes += m
    write_data(out_file, plain_bytes, 'wb')


if __name__ == '__main__':
    gen_key(32)  # 生成公钥文件和私钥文件
    encrypt("./check/users.txt", "./cipherText/enc.txt", './key/publicKey/pub.txt')
    decrypt("./cipherText/enc.txt", "./clearText/dec.txt", './key/privateKey/pri.txt')
