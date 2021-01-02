# encoding: utf-8
# Made By: Lonely_Fantasy💻
# Work Platform: Windows 10 LTSC
# Import File Places
import tkinter
from tkinter import *
from tkinter import Label, ttk, scrolledtext
from func import *
import ui

# -----全局变量----- #
front = []  # 前缀
middile = []  # 中缀
last = []  # 后缀

# -----窗口设置----- #
app = tkinter.Tk()
app.iconbitmap('./calculate.ico')
app.title('表达式转换计算工具')
app.resizable(0, 0)

# ---------------UI部分--------------- #
# -----下拉表选择----- #
select = tkinter.StringVar()  # 模式选择
number_chosen = ttk.Combobox(
    app, width=12, font=("微软雅黑", 9), textvariable=select)
number_chosen['values'] = ('前缀', '中缀', '后缀')
number_chosen.grid(row=0, column=0)

# -----Label控件----- #
front_label = Label(app, text='前缀表达式', font=("微软雅黑", 11)) \
    .grid(row=1, column=0, sticky=W + E)
middile_label = Label(app, text='中缀表达式', font=("微软雅黑", 11)) \
    .grid(row=3, column=0, sticky=W + E)
last_label = Label(app, text='后缀表达式', font=("微软雅黑", 11)) \
    .grid(row=5, column=0, sticky=W + E)

# -----输入框控件----- #
front_text = scrolledtext.ScrolledText(
    app, width=50, height=3, font=("微软雅黑", 12))
middile_text = scrolledtext.ScrolledText(
    app, width=50, height=3, font=("微软雅黑", 12))
last_text = scrolledtext.ScrolledText(
    app, width=50, height=3, font=("微软雅黑", 12))
front_text.grid(row=2, column=0)
middile_text.grid(row=4, column=0)
last_text.grid(row=6, column=0)

# -----Button控件----- #
Button(app, text='一键转换', font=("微软雅黑", 12), width=10) \
    .grid(row=7, column=0, sticky=W+E, padx=5, pady=3)
Button(app, text='使用帮助', font=("微软雅黑", 12), width=10) \
    .grid(row=8, column=0, sticky=W, padx=5, pady=3)
Button(app, text='一键清空', font=("微软雅黑", 12), width=10) \
    .grid(row=8, column=0, sticky=E, padx=5, pady=3)
# 123

# ---------------END--------------- #

app.mainloop()
