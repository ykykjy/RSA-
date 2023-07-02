# 基于RSA算法的加密系统
## 1. python所用库
### 1.1 ttkbootstrap
> ttkbootstrap 是一个基于 tkinter 的界面美化库，使用这个工具可以开发出类似前端 bootstrap 风格的 tkinter 桌面程序,[ttkbootstrap官方文档](https://ttkbootstrap.readthedocs.io/en/latest/)
##### 1. 安装步骤
```bash
pip install ttkbootstrap -i https://pypi.douban.com/simple/
```

##### 2. 简单使用
```python
import ttkbootstrap as ttk
root = ttk.Window(
        title="窗口名字",        #设置窗口的标题
        themename="litera",     #设置主题
        size=(1066,600),        #窗口的大小
        position=(100,100),     #窗口所在的位置
        minsize=(0,0),          #窗口的最小宽高
        maxsize=(1920,1080),    #窗口的最大宽高
        resizable=None,         #设置窗口是否可以更改大小
        alpha=1.0,              #设置窗口的透明度(0.0完全透明）
        )
root.geometry('1000x600')  # 设置窗口可最大伸展的大小
# root.place_window_center()    #让显现出的窗口居中
# root.resizable(False,False)   #让窗口不可更改大小
# root.wm_attributes('-topmost', 1)#让窗口位置其它窗口之上
root.mainloop()
```

### 1.2 PIL
>  PIL库是图像处理的库，具有强大图像处理能力，不仅包含了丰富的像素、色彩操作功能，还可以用于图像归档和批量处理
##### 1. 安装步骤
```bash
pip install pillow -i https://pypi.douban.com/simple/
```

##### 2. 简单使用
> [PIL详细使用教程](https://blog.csdn.net/qq_41854911/article/details/122697049)


## 2. 基础知识

## 3. 遇到的问题
#### 3.1 安装Crypto
> Crypto是一个比较特殊的库，安装分为如下几步：
1. 关闭VPN
2. `pip install pycryptodome`
3. 在venv/Lib/site-packages中把crypto改为Crypto
> 进行如上三步就大功告成了


## 4. 功能模块划分
### 4.1 rsa算法加密
### 4.2 ECC算法验证文件完整性
![]()


