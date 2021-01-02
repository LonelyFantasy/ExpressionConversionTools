class check():
    def become_list_v2(words_1):
        flag=1
        for key in words_1:
            if not key in '+-*/()0123456789{}[]':
                flag=0
                break;
        return flag


class calculate():
    # -----缩写提示：front:f   middile:m   last:l----- #

    def f_to_m(list):    # 前转中缀
        print('1')

    def m_to_l(list):    # 中转后缀
        print('2')

    def l_to_m(list):    # 后转中缀
        print('3')

    def m_to_f(list):    # 中转前缀
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

    def value(list):    # 后缀求值
        lista = []
        for a in list:
            if isinstance(a, int):  # 遇见数字直接入栈
                lista.insert(0, a)
                print(lista)
            elif a == '+':  # 遇见符号把栈中两个数字弹出，这两个数字运算后把结果入栈
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, b+c)
            elif a == '-':
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, c-b)
            elif a == '*':
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, b*c)
            elif a == '/':
                b = lista[0]
                del lista[0]
                c = lista[0]
                del lista[0]
                lista.insert(0, c/b)
        return lista[0]  # 栈中最后的元素就是结果
    
