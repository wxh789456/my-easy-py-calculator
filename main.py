"""
main.py

这个文件是程序入口。
负责和用户交互，但不直接处理计算逻辑。
"""

from calculator import calculate
from validator import to_number, is_valid_operator


def show_welcome():
    print("欢迎使用简易计算器")


def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return to_number(value)
        except ValueError as e:
            print(e)


def get_operator():
    while True:
        value = input("op:").strip()
        if is_valid_operator(value):
            return value
        else:
            print("操作符非法")


def ask_continue():
    while 1:
        choice = input("是否继续计算？[y/n]:").strip().lower()
        if choice == 'y':
            return True
        else:
            return False


def run_calculator():
    show_welcome()
    while 1:
        a = get_number("a:")
        op = get_operator()
        b = get_number("b:")

        try:
            print("output:", calculate(a, b, op))
        except ValueError as e:
            print(e)
        if ask_continue() == False:
            break


if __name__ == "__main__":
    run_calculator()
