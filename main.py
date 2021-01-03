# encoding: utf-8
# Made By: Lonely_Fantasy💻
# Work Platform: Windows 10 LTSC
# Import File Places
import tkinter
import ui
import base64
import os
import func
from tkinter import *
from tkinter import Label, ttk, scrolledtext
from icon import Icon


# -----全局变量----- #
front = []  # 前缀
middile = []  # 中缀
last = []  # 后缀

# -----窗口设置----- #
app = tkinter.Tk()
app.title('表达式转换计算工具')
app.resizable(0, 0)

# -----图标base64转码----- #
with open('tmp.ico', 'wb') as tmp:
    tmp.write(base64.b64decode(Icon().img))
app.iconbitmap('tmp.ico')
os.remove('tmp.ico')

'''
sw = app.winfo_screenwidth()#得到屏幕宽度
sh = app.winfo_screenheight()#得到屏幕高度
x = (sw-610) / 2
y = (sh-400) / 2
app.geometry("%dx%d+%d+%d" %(610,400,x,y))
'''

# ---------------界面部分--------------- #
# -----下拉表选择----- #
number = tkinter.StringVar()
number_chosen = ttk.Combobox(
    app, width=12, font=("微软雅黑", 9), textvariable=number)
number_chosen['values'] = ('前缀表达式', '中缀表达式', '后缀表达式')
number_chosen.grid(row=0, column=0)
number_chosen.current(1)

# -----Label控件----- #
front_label = Label(app, text='前缀表达式', font=("微软雅黑", 11)) \
    .grid(row=1, column=0, sticky=W + E)
middile_label = Label(app, text='中缀表达式', font=("微软雅黑", 11)) \
    .grid(row=3, column=0, sticky=W + E)
last_label = Label(app, text='后缀表达式', font=("微软雅黑", 11)) \
    .grid(row=5, column=0, sticky=W + E)
result_label = Label(app, text='计算结果', font=("微软雅黑", 11))\
    .grid(row=7, column=0, sticky=W + E)
choosen_label = Label(app, text='转换式子选择👉', font=("微软雅黑", 11)) \
    .grid(row=0, column=0, sticky=W)
choosen_label = Label(app, text='👈转换式子选择', font=("微软雅黑", 11)) \
    .grid(row=0, column=0, sticky=E)

# -----输入框控件----- #
front_text = scrolledtext.ScrolledText(
    app, width=50, height=3, font=("微软雅黑", 12))
middile_text = scrolledtext.ScrolledText(
    app, width=50, height=3, font=("微软雅黑", 12))
last_text = scrolledtext.ScrolledText(
    app, width=50, height=3, font=("微软雅黑", 12))
result_text = scrolledtext.ScrolledText(
    app, width=50, height=2, font=("微软雅黑", 12))
front_text.grid(row=2, column=0)
middile_text.grid(row=4, column=0)
last_text.grid(row=6, column=0)
result_text.grid(row=8, column=0)

# -----Button控件----- #
Button(app, text='一键转换', font=("微软雅黑", 12), width=10, command=lambda: schecude()) \
    .grid(row=9, column=0, sticky=W+E, padx=5, pady=3)
Button(app, text='使用帮助', font=("微软雅黑", 12), width=10, command=lambda: ui.show_help()) \
    .grid(row=10, column=0, sticky=W, padx=5, pady=3)
Button(app, text='一键清空', font=("微软雅黑", 12), width=10, command=lambda: ui.clean_box(front_text, middile_text, last_text, result_text)) \
    .grid(row=10, column=0, sticky=E, padx=5, pady=3)
Button(app, text='填写帮助', font=("微软雅黑", 12), width=10, command=lambda: ui.clean_box(front_text, middile_text, last_text, result_text)) \
    .grid(row=10, column=0, padx=5, pady=3)

# -----版权显示----- #
banquan = Label(app, text='©2021 Design By Team Menber', font=("微软雅黑", 11)) \
    .grid(row=11, column=0, sticky=W + E)

# ---------------END--------------- #

# -----执行函数----- #


def schecude():
    global front, middile, last
    for a in front_text.get('0.0', END):
        front.append(a)
    for a in middile_text.get('0.0', END):
        middile.append(a)
    for a in last_text.get('0.0', END):
        last.append(a)
    front.pop()
    middile.pop()
    last.pop()
    # Debug
    print(len(front), len(middile), len(last))
    print(number_chosen.current())
    current_number = number_chosen.current()
    if func.check.only_one(front, middile, last, current_number) is False:
        ui.show_warning('你所选的'+number_chosen.get()+'未填写式子\n请重新输入')
        return


app.mainloop()
