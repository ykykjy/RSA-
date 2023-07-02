import hashlib
import ecdsa
from RSA import *

private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key = private_key.get_verifying_key()


def get_file_hash(file_path):
    """
    计算文件hash值
    :param file_path: 要计算hash值的文件路径
    :return: 返回文件的hash值
    """
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return hashlib.sha256(file_data).hexdigest()


def sign_file():
    """
    对文件进行签名(使用hash算法得到文件的唯一标识)
    """
    file_path = get_op_filename()  # file_path: 文件路径
    file_hash = get_file_hash(file_path)
    signature = private_key.sign(file_hash.encode())  # 私钥对hash值进行加密
    with open('./identifies/sign.txt', 'wb') as fp:
        fp.write(signature)
    Message(temp_window, text="文件签名成功").place(x=400, y=100, width=200, height=100)


def checkx():
    """
    验证文件签名,根据signature验证文件完整性
    """
    file_path = get_op_filename()  # file_path: 文件路径
    with open('./identifies/sign.txt', 'rb') as fp:
        signature = fp.read()  # signature: 文件唯一标识
    file_hash = get_file_hash(file_path)  # 生成文件的hash值
    try:
        public_key.verify(signature, file_hash.encode())  # 用公钥进行解密，并与生成的hash值进行比较
        return True
    except ecdsa.BadSignatureError:
        return False


def verify_file():
    """
    验证文件签名是不是完整的
    """
    result = checkx()
    if result:
        Message(temp_window, text="文件是完整的").place(x=400, y=100, width=200, height=100)
    else:
        Message(temp_window, text="文件不是完整的").place(x=400, y=100, width=200, height=100)
