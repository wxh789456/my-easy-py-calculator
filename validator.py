"""
validator.py

这个文件负责检查用户输入是否合法。
例如：
1. 判断输入是不是数字
2. 判断运算符是否合法
3. 把用户输入的字符串转换成数字
"""


def is_valid_number(value):
    try:
        value = float(value)
        return True
    except ValueError:
        return False


def to_number(value):
    if not is_valid_number(value):
        raise ValueError("请输入合法的数字")
    return float(value)


def is_valid_operator(op):
    return op in ('+', '-', '*', '/')
