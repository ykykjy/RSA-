import sys
from PIL import ImageTk, Image
from tkinter import filedialog
from cryinrsa import *
from tkinter import Message


pub_key_filename = ""
priv_key_filename = ""
op_filename = ""
temp_window = None


def get_op_filename():
    """
    获取要加解密的文件的绝对路径
    :return: 文件绝对路径
    """
    global op_filename  # op_filename为要加解密的文件路径
    op_filename = filedialog.askopenfilename(title='选择文件', filetypes=[("所有文件", "*.*")], initialdir='./',
                                             parent=temp_window)
    return op_filename


def decrypt_op_file():
    """
    对文件进行解密
    """
    get_op_filename()  # 解密文件
    Message(temp_window, text="已开始解密")
    decrypt(op_filename, "./clearText/dec.txt", priv_key_filename)  # op_filename为要解密的文件路径，dec.txt为解密后文件存放的路径
    Message(temp_window, text="解密文件：clearText/dec.txt").place(x=400, y=100, width=200, height=100)


def encrypt_op_file():
    """
    对文件进行加密
    """
    get_op_filename()
    encrypt(op_filename, "./cipherText/enc.txt", pub_key_filename)  # op_filename为要加密的文件路径，enc.txt为加密后字节存放的文件路径
    Message(temp_window, text="加密文件：cipherText/enc.txt").place(x=400, y=100, width=200, height=100)


def get_pub_key_filename():
    """
    获取公钥文件函数
    :return:  公钥文件的绝对路径
    """
    global pub_key_filename
    pub_key_filename = filedialog.askopenfilename(title='选择文件', filetypes=[("所有文件", "*.*")], initialdir='./',
                                                  parent=temp_window)
    print(pub_key_filename)


def get_priv_key_filename():
    """
    获取私钥文件函数
    :return: 返回私钥文件绝对路径
    """
    global priv_key_filename
    priv_key_filename = filedialog.askopenfilename(title='选择文件', filetypes=[("所有文件", "*.*")], initialdir='./',
                                                   parent=temp_window)


def get_img(filename, width, height):
    """
    对图像进行处理
    :param filename: 图片地址
    :param width: 图片宽度
    :param height: 图片高度
    :return:  <class 'PIL.ImageTk.PhotoImage'>对象
    """
    im = Image.open(filename).resize((width, height))  # 给图像设置宽高
    im = ImageTk.PhotoImage(im)  # <class 'PIL.ImageTk.PhotoImage'>
    return im


def check(account, password):
    """
    确定该用户是不是指定用户
    :param account: 用户名
    :param password: 密码
    :return: 如果用户名和密码错误就停止运行
    """
    total = account + password
    with open('./check/users.txt', 'r') as fp:
        result = fp.read()
        if total == result:
            print("账户密码正确，登录成功")
        else:
            print("账户密码正确，登录失败")
            sys.exit()
