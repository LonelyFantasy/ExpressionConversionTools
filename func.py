# encoding: utf-8
from pythonds.basic.stack import Stack
import copy


class Node:
    def __init__(self, data):
        self.left = None  # 左节点
        self.right = None  # 右节点
        self.data = data  # 值

    def PrintTree(self):
        print(self.data)


class Tree:
    def hfoot(root, list):  # 中序遍历二叉树插入栈,得到较复杂表达式
        if root == None:
            return
        if isinstance(root.data, int) != 1:
            list.insert(0, '(')
        Tree.hfoot(root.left, list)
        list.insert(0, root.data)
        Tree.hfoot(root.right, list)
        if isinstance(root.data, int) != 1:
            list.insert(0, ')')

    def find_brackets(list, left, right):  # 找括号的左右运算优先级
        llevel = rlevel = 0
        if left != 0:
            i = left - 1
            if list[i] == '+' or list[i] == '-':
                llevel = 1
            elif list[i] == '*' or list[i] == '/':
                llevel = 2
            elif list[i] == ')':
                llevel = 3
            elif list[i] == '(':
                llevel = 0
        if right + 1 != len(list):
            i = right + 1
            if list[i] == '+' or list[i] == '-':
                rlevel = 1
            elif list[i] == '*' or list[i] == '/':
                rlevel = 2
            elif list[i] == '(':
                rlevel = 3
            elif list[i] == ')':
                rlevel = 0
        if llevel > rlevel:
            return llevel
        else:
            return rlevel

    def delbrackets(list):  # 删除括号，最终化简表达式
        del list[0]
        del list[-1]
        q = 0
        while (q < len(list)):
            start = end = -1
            num = 0
            level = elevel = 0
            op = None
            for i in range(q, len(list)):
                if list[i] == '(':
                    num += 1
                    if start == -1:
                        start = i
                elif (list[i] == '+' or list[i] == '-' or list[i] == '*' or list[i] == '/') and num == 1:
                    op = list[i]
                elif list[i] == ')':
                    num -= 1
                    if num == 0:
                        end = i
                        if op == '+' or op == '-':
                            level = 1
                        elif op == '*' or op == '/':
                            level = 2
                        elevel = Tree.find_brackets(list, start, end)
                        if level >= elevel:  # 若括号左右优先级比之较小，则删除括号
                            del list[end]
                            del list[start]
                        break
            if (start != -1):
                q = start
            q += 1


class Pretreatment:  # 内容识别处理
    def decimal_recognition(cur_list):  # 废弃函数
        """
        :cur_list: list
        """
        i = flag = head = tail = 0
        temp = []  # 缓存小数
        result = []  # 结果缓存
        length = len(cur_list)
        while i < length:
            if cur_list[i] == '#' and flag == 0:  # 划分小数区域
                flag = 1
                head = i
            elif cur_list[i] == '#' and flag == 1:
                flag = 2
                tail = i
            if flag == 1:  # 是否开始识别
                i = i + 1
                if i == length:  # 识别符号残缺情况，有就报错
                    return -1
                continue
            elif flag == 2:  # 识别小数区域是否划分完成
                if head == tail - 1:  # 防止出现'##'情况
                    i = i + 1
                    continue
                for m in range(head + 1, tail):
                    temp.append(cur_list[m])
                result.append(''.join(temp))
                temp.clear()
                flag = 0
            else:  # 未进入识别，正常复制
                result.append(cur_list[i])
            i = i + 1
        return result

    def trans_to_num(cur_list):  # 字符转数字+空格处理
        """
        :cur_list: list
        """
        i = 0
        temp = []  # 内容缓存
        temp2 = []  # 数字判断
        result = []  # 结果保存
        length = len(cur_list)
        for i in cur_list:
            if i == ' ' and len(temp):  # 检测到空格且缓存中有内容
                if temp[0] == ' ':  # 防多空格
                    temp.remove(' ')
                temp2.append(''.join(temp))
                if not len(temp):  # 防多空格
                    continue
                if temp2[0] not in '+-*/()':
                    result.append(int(''.join(temp)))
                    temp.clear()
                    temp2.clear()
                else:
                    result.append(''.join(temp))
                    temp.clear()
                    temp2.clear()
            else:
                temp.append(i)
        if len(temp) and temp[0] == ' ':  # 防多空格
            temp.remove(' ')
        if len(temp):
            temp2.clear()
            temp2.append(''.join(temp))
            if temp2[0] not in '+-*/()':
                result.append(int(''.join(temp)))
                temp.clear()
                temp2.clear()
            else:
                result.append(''.join(temp))
                temp.clear()
                temp2.clear()
        return result


class Check:
    def symbol(cur_list):
        """
        :cur_list: list
        """
        print(cur_list)
        for key in cur_list:
            if not key in '+-*/()0123456789 ':
                return False
        return True

    def is_balance(list):  # 检查括号是否平衡
        result_stack = Stack()
        for i in list:
            if i in ['{', '[', '(']:
                result_stack.push(i)
            elif i in ['}', ']', ')']:  # 遇到结束括号的情况
                if result_stack.isEmpty():  # 如果当前栈为空, 不匹配,返回False
                    return False
                chFromStack = result_stack.pop()
                if not ((chFromStack == '{' and i == '}')
                        or (chFromStack == '[' and i == ']')
                        or (chFromStack == '(' and i == ')')):
                    # 如果不满足匹配条件, 则返回False
                    return False
        # 遍历结束后, 如果结果栈为空, 则代表括号匹配, 栈不为空, 括号不匹配
        return result_stack.isEmpty()

    def only_one(front, middile, last, current):  # 判断是否填写数据并清空无用list
        """
        :front: list
        :middile: list
        :last: list
        """
        if current == 0:
            if len(front):
                middile.clear()
                last.clear()
            else:
                return False
        elif current == 1:
            if len(middile):
                front.clear()
                last.clear()
            else:
                return False
        else:
            if len(last):
                front.clear()
                middile.clear()
            else:
                return False
        return True


class calculate():
    # -----缩写提示：front:f   middile:m   last:l----- #
    def f_to_m(cur_list):  # 前转中缀
        """
        :cur_list: list
        """
        temp = []
        s = Stack()
        list = [str(i) for i in cur_list]
        for par in list:
            if par in "+-*/":  # 遇到运算符则入栈
                s.push(par)
            else:  # 为数字时分两种情况：
                if s.peek() in '+-*/':  # 栈顶为运算符
                    s.push(par)  # 数字入栈
                else:  # 当前栈顶为数字
                    while (not s.isEmpty()) and (not s.peek() in '+-*/'):  # 若栈不空，且当前栈顶为数字，则循环计算
                        shu = s.pop()  # 运算符前的数字出栈
                        fu = s.pop()  # 运算符出栈
                        if fu == '+' or fu == '-':
                            if s.size() == 0:  # 最后一次运算不需要括号，无论什么运算符
                                par = shu + fu + par
                                break
                            par = '(' + shu + fu + par + ')'  # 计算
                        else:  # 乘除不需要括号
                            par = shu + fu + par  # 计算
                    s.push(str(par))  # 算式入栈
        list1 = (str(s.pop()))  # 用列表存新的算式
        for i in list1:
            if i not in '+-*/()':
                temp.append(int(i))
            else:
                temp.append(i)
        print(temp)
        return temp  # 返回最终算式

    def m_to_l(expression):
        result = []  # 结果列表
        stack = []  # 栈
        for item in expression:
            if isinstance(item, int):  # 如果当前字符为数字那么直接放入结果列表
                result.append(item)
            else:  # 如果当前字符为一切其他操作符
                if len(stack) == 0:  # 如果栈空，直接入栈
                    stack.append(item)
                elif item in '*/(':  # 如果当前字符为*/（，直接入栈
                    stack.append(item)
                elif item == ')':  # 如果右括号则全部弹出（碰到左括号停止）
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                # 如果当前字符为加减且栈顶为乘除，则开始弹出
                elif item in '+-' and stack[len(stack) - 1] in '*/':
                    if stack.count('(') == 0:  # 如果有左括号，弹到左括号为止
                        while stack:
                            result.append(stack.pop())
                    else:  # 如果没有左括号，弹出所有
                        t = stack.pop()
                        while t != '(':
                            result.append(t)
                            t = stack.pop()
                        stack.append('(')
                    stack.append(item)  # 弹出操作完成后将‘+-’入栈
                else:
                    stack.append(item)  # 其余情况直接入栈（如当前字符为+，栈顶为+-）

        # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
        while stack:
            result.append(stack.pop())
        # 返回字符串

        return result

    def l_to_m(list):  # 后转中缀
        lista = []  # 建立空的数字栈
        listb = []  # 建立符号栈，放入一个元素避免引用出错
        for a in list:
            if isinstance(a, int):  # 遇见数字直接压入数字栈
                root = Node(a)  # 创建节点
                lista.insert(0, root)
            else:
                root = Node(a)  # 创建节点
                root.right = lista[0]
                del lista[0]
                root.left = lista[0]
                del lista[0]
                lista.insert(0, root)
        Tree.hfoot(root, listb)
        listb.reverse()
        Tree.delbrackets(listb)
        return listb

    def m_to_f(cur_list):  # 中转前缀
        list = copy.deepcopy(cur_list)
        list.reverse()
        lista = []  # 建立空的数字栈
        listb = [0]  # 建立符号栈，放入一个元素避免引用出错
        for a in list:
            if isinstance(a, int):  # 遇见数字直接压入数字栈
                lista.insert(0, a)

            elif a == '(':  # 遇见'('遍历符号栈把符号栈中元素取出放入数字栈中直到遇见‘）’，然后把‘）‘从符号栈中删除
                while listb[0] != ')':
                    lista.insert(0, listb[0])
                    del listb[0]
                del listb[0]
            else:
                if listb[0] == 0:  # 如果符号栈为空，直接入符号栈
                    listb.insert(0, a)
                else:
                    if listb[0] == ')':  # 如果符号栈栈顶元素是’）‘，直接入符号栈
                        listb.insert(0, a)
                    elif a == '*' or a == '/' or a == ')':  # 如果符号优先级大于符号栈栈顶元素，直接入栈
                        listb.insert(0, a)
                    # 如果符号优先级等于符号栈栈顶元素，直接入栈
                    elif (a == '-' or a == '+') and (listb[0] == '-' or listb[0] == '+'):
                        listb.insert(0, a)
                        # 如果符号优先级小于符号栈栈顶元素，则把元素取出放入数字栈直到优先级相等或者符号栈变为空
                    elif (a == '-' or a == '+') and (listb[0] == '*' or listb[0] == '/'):
                        for c in listb:
                            if c == '*' or c == '/':
                                del listb[0]
                                lista.insert(0, c)
                            elif c == '+' or c == '-':
                                listb.insert(0, a)
                                break
                        listb.insert(0, a)
        for c in listb:  # 把剩余符号栈中元素取出放入数字栈
            lista.insert(0, c)
        del lista[0]  # 把0从数字栈栈顶删除避免影响结果
        return lista

    def get_value(cur_list):  # 后缀求值
        lista = []
        for a in cur_list:
            if isinstance(a, int):  # 遇见数字直接入栈
                lista.insert(0, a)
                print(lista)
            elif a == '+':  # 遇见符号把栈中两个数字弹出，这两个数字运算后把结果入栈
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, b + c)
            elif a == '-':
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, c - b)
            elif a == '*':
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, b * c)
            elif a == '/':
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, c / b)
        return lista[0]  # 栈中最后的元素就是结果
