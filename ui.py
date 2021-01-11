# encoding: utf-8
from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext
import sys
import webbrowser

class Window():
    def show_help():
        tkinter.messagebox.showinfo(
            "使用帮助",
            "Version: Release 1.0\n\n"
            "选择需要转换的前中后缀\n"
            "并在相应的框内输入式子\n"
            "完成后点击一键转换\n")


    def show_edit():
        tkinter.messagebox.showinfo(
            '输入说明',
            '1. 任何式子仅支持英文符号输入\n'
            '2. 前缀、后缀表达式的符号与数字间请使用空格分隔')


    def show_warning(msg):
        tkinter.messagebox.showwarning("提示", msg)


    def show_wrong(msg):
        Window.show_warning('你所选的' + msg + '式子有误\n请重新输入')


    def quit_waining():
        value = tkinter.messagebox.askyesno('退出程序', '确认退出？')
        if value:
            sys.exit(0)
        else:
            return


def open_url(event):
    webbrowser.open("https://github.com/LonelyFantasy/ExpressionConversionTools", new=0)

class Clean():
    def select_box(front_text, middile_text, last_text, result_text, current_number):
        """
        :front_text: scrolledtext
        :middile_text: scrolledtext
        :last_text: scrolledtext
        :result_text: scrolledtext
        """
        if current_number == 0:
            middile_text.delete(1.0, END)
            last_text.delete(1.0, END)
        elif current_number == 1:
            front_text.delete(1.0, END)
            last_text.delete(1.0, END)
        else:
            front_text.delete(1.0, END)
            middile_text.delete(1.0, END)
        result_text.config(state=NORMAL)
        result_text.delete(1.0, END)
        
    def all_box(front_text, middile_text, last_text, result_text):
        """
        :front_text: scrolledtext
        :middile_text: scrolledtext
        :last_text: scrolledtext
        :result_text: scrolledtext
        """
        last_text.delete(1.0, END)
        front_text.delete(1.0, END)
        middile_text.delete(1.0, END)
        result_text.config(state=NORMAL)
        result_text.delete(1.0, END)

