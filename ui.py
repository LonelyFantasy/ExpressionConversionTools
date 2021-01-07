# encoding: utf-8
from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext
import sys
import webbrowser


def show_help():
    tkinter.messagebox.showinfo(
        "使用帮助",
        "Version: Bata1.0\n\n"
        "选择需要转换的前中后缀\n"
        "并在相应的框内输入式子\n"
        "完成后点击一键转换\n")


def show_edit():
    tkinter.messagebox.showinfo(
        '格式帮助',
        '输入样例：( 1 + 2 ) * 3\n\n'
        '任何式子仅支持英文符号输入\n'
        '符号与数字间请使用空格分隔')


def show_warning(msg):
    tkinter.messagebox.showwarning("提示", msg)


def show_wrong(msg):
    show_warning('你所选的' + msg + '式子有误\n请重新输入')


def quit_waining():
    value = tkinter.messagebox.askyesno('退出程序', '确认退出？')
    if value:
        sys.exit(0)
    else:
        return


def open_url(event):
    webbrowser.open("https://github.com/LonelyFantasy/ExpressionConversionTools", new=0)


def clean_box(front_text, middile_text, last_text, result_text):
    """
    :front_text: scrolledtext
    :middile_text: scrolledtext
    :last_text: scrolledtext
    :result_text: scrolledtext
    """
    front_text.delete(1.0, END)
    middile_text.delete(1.0, END)
    last_text.delete(1.0, END)
    result_text.config(state=NORMAL)
    result_text.delete(1.0, END)

