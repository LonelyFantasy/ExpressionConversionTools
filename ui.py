# encoding: utf-8
from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext
import sys


def show_help():
    tkinter.messagebox.showinfo(
        "使用帮助",
        "选择需要转换的前中后缀\n"
        "并在相应的框内输入式子\n"
        "完成后点击一键转换\n")


def show_warning(msg):
    tkinter.messagebox.showwarning("提示", msg)


def quit_waining():
    value = tkinter.messagebox.askyesno('退出程序', '确认退出？')
    if value:
        sys.exit(0)
    else:
        return


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
    result_text.delete(1.0, END)