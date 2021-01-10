# encoding: utf-8
# Made By: Lonely_Fantasy💻
# Work Platform: Windows 10 LTSC
# Import File Places
import tkinter
import ui
import base64
import os
import func
import copy
from tkinter import *
from tkinter import Label, ttk, scrolledtext, END, NORMAL, DISABLED, W, E
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
result_label = Label(app, text='计算结果', font=("微软雅黑", 11)) \
    .grid(row=7, column=0, sticky=W + E)
choosen_label = Label(app, text='转换式子选择👉', font=("微软雅黑", 11)) \
    .grid(row=0, column=0, sticky=W)
choosen_label = Label(app, text='👈转换式子选择', font=("微软雅黑", 11)) \
    .grid(row=0, column=0, sticky=E)
yangli1 = Label(app, text='样例：+ + 1 23 4', font=("微软雅黑", 11)) \
    .grid(row=1, column=0, sticky=E)
middile_label = Label(app, text='样例：(1+23)+4', font=("微软雅黑", 11)) \
    .grid(row=3, column=0, sticky=E)
last_label = Label(app, text='样例：1 23 + 4 +', font=("微软雅黑", 11)) \
    .grid(row=5, column=0, sticky=E)

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
    .grid(row=9, column=0, sticky=W + E, padx=5, pady=3)
Button(app, text='使用帮助', font=("微软雅黑", 12), width=10, command=lambda: ui.Window.show_help()) \
    .grid(row=10, column=0, sticky=W, padx=5, pady=3)
Button(app, text='一键清空', font=("微软雅黑", 12), width=10,
       command=lambda: ui.Clean.all_box(front_text, middile_text, last_text, result_text)) \
    .grid(row=10, column=0, sticky=E, padx=5, pady=3)
Button(app, text='输入说明', font=("微软雅黑", 12), width=10,
       command=lambda: ui.Window.show_edit()) \
    .grid(row=10, column=0, padx=5, pady=3)

# -----版权显示----- #
banquan1 = tkinter.Label(app, text='©2021 Powered By 黎炳材小组', font=("微软雅黑", 11))\
    .grid(row=11, column=0, sticky=W)
banquan2 = tkinter.Label(
    app, text='👉Design By LonelyFantasy', font=("微软雅黑", 11, UNDERLINE))
banquan2.grid(row=11, column=0, sticky=E)
banquan2.bind("<Button-1>", ui.open_url)
# ---------------END--------------- #

# ---------------核心流程函数（勿动）--------------- #

# -----输出结果----- #
def output_data(result):
    global front, middile, last
    # -----框初始化----- #
    front_text.delete(1.0, END)
    middile_text.delete(1.0, END)
    last_text.delete(1.0, END)
    front_text.insert(END, " ".join(str(l) for l in front))
    middile_text.insert(END, "".join(str(l) for l in middile))
    last_text.insert(END, " ".join(str(l) for l in last))
    result_text.config(state=NORMAL)
    result_text.delete(1.0, END)
    result_text.insert(END, result)
    result_text.config(state=DISABLED)

# -----转换按钮函数----- #

def schecude():
    global front, middile, last
    # 刷新list
    front.clear()
    middile.clear()
    last.clear()
    result_text.delete(1.0, END)
    for a in front_text.get('0.0', END):
        front.append(a)
    for a in middile_text.get('0.0', END):
        middile.append(a)
    for a in last_text.get('0.0', END):
        last.append(a)
    front.pop()
    middile.pop()
    last.pop()
    current_number = number_chosen.current()
    if not func.Check.only_one(front, middile, last, current_number):
        ui.Window.show_warning('你所选的' + number_chosen.get() + '未填写式子\n请重新输入')
        return
    ui.Clean.select_box(front_text, middile_text, last_text, result_text, current_number)
    # -----前缀流程----- #
    if current_number == 0:  # 选择前缀一系列操作
        if not func.Check.symbol(front):  # 符号判断
            ui.Window.show_wrong(number_chosen.get())
            return
        front = copy.deepcopy(func.Pretreatment.trans_to_num(front))  # 格式化处理
        if func.Check.num_symbol(front) is False:# 数符数量判断
            ui.Window.show_wrong(number_chosen.get())
            return
        middile = copy.deepcopy(func.calculate.f_to_m(front))  # 转中缀做平衡判断
        print('转完到middile检查：:', middile)  # debug
        if func.Check.is_balance(middile) is False:  # 合法性判断
            ui.Window.show_wrong(number_chosen.get())
            return
        if func.Check.num_symbol(middile) is False:# 数符数量判断
            ui.Window.show_wrong(number_chosen.get())
            return
        last = copy.deepcopy(func.calculate.m_to_l(middile))
        print('三缀list存储内容检查：', front, middile, last)  # debug
        print('长度检查：', len(front), len(middile), len(last))  # debug
        output_data(func.calculate.get_value(last))
    # -----中缀流程----- #
    elif current_number == 1:
        if not func.Check.symbol(middile):  # 符号判断
            ui.Window.show_wrong(number_chosen.get())
            return
        # middile = copy.deepcopy(
            # func.Pretreatment.trans_to_num(middile))  # 格式化处理
        middile = copy.deepcopy(func.Pretreatment.middile(middile))
        print('转完到middile检查：:', middile)  # debug
        if  func.Check.is_balance(middile) is False or func.Check.num_symbol(middile) is False:  # 合法性判断
            ui.Window.show_wrong(number_chosen.get())
            return
        front = copy.deepcopy(func.calculate.m_to_f(middile))
        last = copy.deepcopy(func.calculate.m_to_l(middile))
        print('三缀list存储内容检查：', front, middile, last)  # debug
        print('长度检查：', len(front), len(middile), len(last))  # debug
        output_data(func.calculate.get_value(last))
    # -----后缀流程----- #
    elif current_number == 2:
        if not func.Check.symbol(last):  # 符号判断
            ui.Window.show_wrong(number_chosen.get())
            return
        last = copy.deepcopy(func.Pretreatment.trans_to_num(last))  # 格式化处理
        if func.Check.num_symbol(last) is False:# 数符数量判断
            ui.Window.show_wrong(number_chosen.get())
            return
        print(middile)
        middile = copy.deepcopy(func.calculate.l_to_m(last))  # 转中缀做平衡判断
        print('转完到middile检查：:', middile)  # debug
        if func.Check.is_balance(middile)is False:  # 合法性判断
            ui.Window.show_wrong(number_chosen.get())
            return
        if func.Check.num_symbol(middile) is False:# 数符数量判断
            ui.Window.show_wrong(number_chosen.get())
            return
        front = copy.deepcopy(func.calculate.m_to_f(middile))
        print('三缀list存储内容检查：', front, middile, last)  # debug
        print('长度检查：', len(front), len(middile), len(last))  # debug
        output_data(func.calculate.get_value(last))
# ---------------核心流程函数END--------------- #

app.update()
sw = app.winfo_screenwidth()#得到屏幕宽度
sh = app.winfo_screenheight()#得到屏幕高度
ww = app.winfo_width()# 获取当前窗口的宽度
wh = app.winfo_height()# 获取当前窗口高度
x = (sw-ww) / 2
y = (sh-wh) / 2
app.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

app.mainloop()
