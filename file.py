def read_data(file, mode='rb'):
    """
    从文件读出 数据
    :param file:  加解密文件路径
    :param mode:  读取文件的方式
    :return: bytes 数据
    """
    try:
        with open(file, mode=mode) as f:
            data = f.read()
    except FileNotFoundError:
        print('文件不存在:' + file)
    except PermissionError:
        print(f"没有文件{file}读取权限")
    except Exception as e:
        print('其他异常：', e)
    finally:
        f.close()
    return data


def write_data(file, data, mode='wb'):
    """
    把data数据写入文件
    :param file: 加解密后需要写入的文件
    :param data: 写进文件的数据
    :param mode: 把数据写进文件的方式
    """
    try:
        with open(file, mode=mode) as f:
            f.write(data)
    except FileNotFoundError:
        print('文件不存在:' + file)
    except PermissionError:
        print(f"没有文件{file}读取权限")
    except Exception as e:
        print('其他异常：', e)
    finally:
        f.close()
