# -*- coding:utf-8 -*-
import re

def mkdir(path):
    os = __import__('os')

    is_exists = os.path.exists(path)

    if not is_exists:
        os.makedirs(path)
        return True
    else:
        return False


def get_md5(url):
    hashlib = __import__('hashlib')
    if isinstance(url, str):
        url = url.encode(encoding="UTF-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def exclude_none(value):
    if value:
        return value
    else:
        value = "无"
        return value


def extract_num(text):
    # 从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


def extract_num_include_dot(text):
    # 从包含,的字符串中提取出数字
    text_num = text.replace(',', '')
    try:
        nums = int(text_num)
    except:
        nums = -1
    return nums
