"""
calculator.py
这个文件负责计算器的核心计算逻辑。
只处理加、减、乘、除，不处理用户输入和界面显示。
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:  # 注意除数不能为零
        raise ValueError("除数不能为 0")
    return a / b


def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    else:
        raise ValueError("操作符不合法")
