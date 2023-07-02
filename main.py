from integrity import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def login(root, im_root, im_home):
    """
    登录功能实现
    """
    # 设置背景图片
    canvas_root = ttk.Canvas(root, width=1000, height=600)
    canvas_root.create_image(500, 300, image=im_root)
    canvas_root.grid()

    # 输入框
    entry_account = ttk.Entry(root, show=None)
    entry_account.insert('0', '请输入账号')
    entry_account.place(x=180, y=260, width=200, height=30)
    entry_pwd = ttk.Entry(root, show=None)
    entry_pwd.insert('0', '请输入密码')
    entry_pwd.place(x=180, y=310, width=200, height=30)

    # 登录按钮
    btn = ttk.Button(root, text="登录", bootstyle=(PRIMARY, "outline-toolbutton"))
    btn.place(x=180, y=380, width=150, height=40)  # place布局，x代表与图片左边的距离
    btn.bind("<Button-1>", lambda e: home(entry_account.get(), entry_pwd.get(), im_home))  # 监听模式，点击按钮嗲用home()函数
    root.mainloop()


def home(account, password, im_home):
    """
    对文件进行加密的函数
    :param account: 账户
    :param password: 密码
    """
    check(account, password)  # 判断用户账户密码是否正确
    win_home = ttk.Toplevel('root')
    win_home.geometry('1000x600+460+240')
    win_home.title('加密和解密页面')

    # 设置背景图片
    canvas_home = ttk.Canvas(win_home, width=1000, height=600)
    canvas_home.create_image(500, 300, image=im_home)
    canvas_home.grid()
    # 目录扫描
    btn_pub = ttk.Button(win_home, text="进行目录扫描", bootstyle=(PRIMARY, "outline-toolbutton"), command=gen_key(32))
    btn_pub.place(x=400, y=350, width=150, height=40)

    # # 获取公私钥
    # btn_pub = ttk.Button(win_home, text="获取公私钥", bootstyle=(PRIMARY, "outline-toolbutton"), command=gen_key(32))
    # btn_pub.place(x=400, y=350, width=150, height=40)
    #
    # # 选择公钥加密
    # btn_pub = ttk.Button(win_home, text="选择公钥文件", bootstyle=(PRIMARY, "outline-toolbutton"),
    #                      command=get_pub_key_filename)
    # btn_pub.place(x=210, y=250, width=150, height=40)
    #
    # # 选择加密文件
    # btn_encrypt = ttk.Button(win_home, text="选择加密文件", bootstyle=(PRIMARY, "outline-toolbutton"),
    #                          command=encrypt_op_file)
    # btn_encrypt.place(x=210, y=315, width=150, height=40)
    #
    # # 选择私钥解密
    # btn_priv = ttk.Button(win_home, text="选择私钥文件", bootstyle=(PRIMARY, "outline-toolbutton"),
    #                       command=get_priv_key_filename)
    # btn_priv.place(x=595, y=250, width=150, height=40)
    #
    # # 选择解密文件
    # btn_decrypt = ttk.Button(win_home, text="选择解密文件", bootstyle=(PRIMARY, "outline-toolbutton"),
    #                          command=decrypt_op_file)
    # btn_decrypt.place(x=595, y=315, width=150, height=40)
    #
    # # 对文件进行签名
    # btn_decrypt = ttk.Button(win_home, text="对文件进行签名", bootstyle=(PRIMARY, "outline-toolbutton"), command=sign_file)
    # btn_decrypt.place(x=210, y=450, width=150, height=40)
    #
    # # 文件完整性校验
    # btn_decrypt = ttk.Button(win_home, text="文件完整性校验", bootstyle=(PRIMARY, "outline-toolbutton"), command=verify_file)
    # btn_decrypt.place(x=595, y=450, width=150, height=40)


def main():
    root = ttk.Window(title="登录界面")  # 实例化创建应用程序窗口
    root.geometry('1000x600')
    root.resizable(False, False)  # 让窗口不可更改大小
    im_root = get_img('./img/login.jpg', 1000, 600)
    im_home = get_img('./img/home.jpg', 1000, 600)
    login(root, im_root, im_home)


if __name__ == '__main__':
    main()
