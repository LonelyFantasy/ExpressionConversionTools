# encoding: utf-8
import tkinter.messagebox
import sys

def show_warning(msg):
    tkinter.messagebox.showwarning("提示", msg)
    
def quit_waining():
    value = tkinter.messagebox.askyesno('退出程序', '确认退出？')
    if value:
        sys.exit(0)
    else:
        return