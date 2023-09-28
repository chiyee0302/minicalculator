
import tkinter
import tkinter.font
import math

class scienceCalculator(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.all_press_lists = []  # 保存运算数字和符号的列表
        self.is_press_compute = False  # 判断是否按下运算按钮,默认没有按下
        self.result = tkinter.StringVar()  # 显示输入的数字及结果
        self.record = tkinter.StringVar()  # 显示计算过程

    def main(self):
        self.root.minsize(400, 690)  # 显示框的最小长宽
        self.root.title('科学计算器')  # 标题
        #self.root.iconbitmap("./calc.ico")  # 左上角图标

        input_bg, num_fg, btn_fg, btn_background = "#f8f8f8", "#000011", "#000011", "#ffffff"  # 各种颜色
        btn_w, btn_h = 80, 70  # 按钮的长宽

        my_font = tkinter.font.Font(family='微软雅黑', size=20)  # 设置字体
        self.result.set(0)
        self.record.set('')
        # 显示版
        label = tkinter.Label(self.root, font=my_font, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                              textvariable=self.record)
        label.place(width=400, height=120)
        label2 = tkinter.Label(self.root, font=my_font, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                               textvariable=self.result)
        label2.place(y=120, width=400, height=80)
        


        
        btn_change=tkinter.Button(self.root, text='切 换', font=tkinter.font.Font(family='微软雅黑', size=20), bg=btn_background, fg="#49506c", bd=0,
                                command=lambda: self.press_change())
        btn_change.place(x=btn_w * 0, y=0, width=btn_w, height=btn_h/2)

        # 第一行
        btn_ce = tkinter.Button(self.root, text='CE', font=my_font, bg='#cdeeef', fg=btn_fg, bd=0, 
                                command=lambda: self.press_ac('CE'))
        btn_ce.place(x=btn_w * 0, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(self.root, text='C', font=my_font, bg=btn_background, fg=btn_fg, bd=0, 
                                command=lambda: self.press_ac('C'))
        btn_ac.place(x=btn_w * 1, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_back = tkinter.Button(self.root, text='Back', font=my_font, bg=btn_background, fg=btn_fg, bd=0,
                                  command=lambda: self.press_back('b'))
       
        btn_per = tkinter.Button(self.root, text='%', font=my_font, bg=btn_background, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('%'))
        btn_back.place(x=btn_w * 2, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_divi = tkinter.Button(self.root, text='÷', font=my_font, bg=btn_background, fg=btn_fg, bd=0,
                                  command=lambda: self.press_num('/'))
        btn_per.place(x=btn_w * 3, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_divi.place(x=btn_w * 4, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        # 第二行

        btn_asin=tkinter.Button(self.root, text='asin', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('asin'))
        btn_acos= tkinter.Button(self.root, text='acos', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('acos'))
        btn_atan= tkinter.Button(self.root, text='atan', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('atan'))
        btn_log2=tkinter.Button(self.root, text='log2', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('log2'))
        btn_e=tkinter.Button(self.root, text='e', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('e'))
        btn_asin.place(x=btn_w * 0, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_acos.place(x=btn_w * 1, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_atan.place(x=btn_w * 2, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_log2.place(x=btn_w * 3, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_e.place(x=btn_w * 4, y=200 + btn_h * 1, width=btn_w, height=btn_h)




        #第三行
        btn_sin=tkinter.Button(self.root, text='sin', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('sin'))
        btnl= tkinter.Button(self.root, text='(', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('('))
        btnr= tkinter.Button(self.root, text=')', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num(')'))
        btn_mi=tkinter.Button(self.root, text='^', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('^'))
        btn_sqrt=tkinter.Button(self.root, text='√', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('√'))
        btn_sin.place(x=btn_w * 0, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btnl.place(x=btn_w * 1, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btnr.place(x=btn_w * 2, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn_mi.place(x=btn_w * 3, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn_sqrt.place(x=btn_w * 4, y=200 + btn_h * 2, width=btn_w, height=btn_h)

         # 第三行
        btn_cos= tkinter.Button(self.root, text='cos', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('cos'))
        btn_cos.place(x=btn_w * 0, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn7 = tkinter.Button(self.root, text='7', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('7'))
        btn7.place(x=btn_w * 1, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn8 = tkinter.Button(self.root, text='8', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('8'))
        btn8.place(x=btn_w * 2, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn9 = tkinter.Button(self.root, text='9', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('9'))
        btn9.place(x=btn_w * 3, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn_mul = tkinter.Button(self.root, text='×', font=my_font, bg=btn_background, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('*'))
        btn_mul.place(x=btn_w * 4, y=200 + btn_h * 3, width=btn_w, height=btn_h)

        # 第四行
        btn_tan = tkinter.Button(self.root, text='tan', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('tan'))
        btn_tan.place(x=btn_w * 0, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        btn4 = tkinter.Button(self.root, text='4', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('4'))
        btn4.place(x=btn_w * 1, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        btn5 = tkinter.Button(self.root, text='5', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('5'))
        btn5.place(x=btn_w * 2, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        btn6 = tkinter.Button(self.root, text='6', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('6'))
        btn6.place(x=btn_w * 3, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        btn_sub = tkinter.Button(self.root, text='-', font=my_font, bg=btn_background, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('-'))
        btn_sub.place(x=btn_w * 4, y=200 + btn_h * 4, width=btn_w, height=btn_h)

        # 第五行
        btn_log = tkinter.Button(self.root, text='ln', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('ln'))
        btn_log.place(x=btn_w * 0, y=200 + btn_h * 5, width=btn_w, height=btn_h)
        btn1 = tkinter.Button(self.root, text='1', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('1'))
        btn1.place(x=btn_w * 1, y=200 + btn_h * 5, width=btn_w, height=btn_h)
        btn2 = tkinter.Button(self.root, text='2', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('2'))
        btn2.place(x=btn_w * 2, y=200 + btn_h * 5, width=btn_w, height=btn_h)
        btn3 = tkinter.Button(self.root, text='3', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('3'))
        btn3.place(x=btn_w * 3, y=200 + btn_h * 5, width=btn_w, height=btn_h)
        btn_add = tkinter.Button(self.root, text='+', font=my_font, bg=btn_background, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('+'))
        btn_add.place(x=btn_w * 4, y=200 + btn_h * 5, width=btn_w, height=btn_h)

        # 第六行
        btn_ln =  tkinter.Button(self.root, text='lg', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('lg'))
        btn_ln.place(x=btn_w * 0, y=200 + btn_h * 6, width=btn_w , height=btn_h)
        btn_pai =  tkinter.Button(self.root, text='π', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('π'))
        btn_pai.place(x=btn_w * 1, y=200 + btn_h * 6, width=btn_w , height=btn_h)
        btn0 = tkinter.Button(self.root, text='0', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                              command=lambda: self.press_num('0'))
        btn0.place(x=btn_w * 2, y=200 + btn_h * 6, width=btn_w , height=btn_h)
        btn_point = tkinter.Button(self.root, text='.', font=my_font, bg=btn_background, fg=num_fg, bd=0,
                                   command=lambda: self.press_num('.'))
        btn_point.place(x=btn_w * 3, y=200 + btn_h * 6, width=btn_w, height=btn_h)
        btn_equ = tkinter.Button(self.root, text='=', bg='#00bbbe', font=my_font, fg=num_fg, bd=0,
                                 command=lambda: self.press_equal())
        btn_equ.place(x=btn_w * 4, y=200 + btn_h * 6, width=btn_w, height=btn_h)
        self.root.mainloop()


    #按下change
    def press_change(self):
        self.root.destroy()
        my_calculator = Calculator()
        my_calculator.main()





    # 按下数字
    def press_num(self, num):
        if self.is_press_compute is True:  # 如果判断等号按键被按下
            self.record.set("")
            self.result.set(0)  # 清空self.result
            self.is_press_compute = False
        
        # 判断界面的数字是否为0
        old_num = self.result.get()
        new_num=[]
        if old_num == '0' and num != '.':
            new_num=num
            
        else:
            new_num = old_num+num
            
        
        #判断特殊的符号
        if num == '^':
            num='**'
        elif num == '√':
            num='math.sqrt('
            new_num+='('
        elif num == 'sin':
            num='math.sin('
            new_num+='('
        elif num == 'cos':
            num='math.cos('
            new_num+='('
        elif num == 'tan':
            num='math.tan('
            new_num+='('
        elif num == 'lg':
            num='math.log10('
            new_num+='('
        elif num == 'ln':
            num='math.log('
            new_num+='('
        elif num == 'π':
            num='math.pi'
        elif num == 'asin':
            num='math.asin('
            new_num+='('
        elif num == 'acos':
            num='math.acos('
            new_num+='('
        elif num == 'atan':
            num='math.atan('
            new_num+='('
        elif num == 'e':
            num='math.e'
        elif num == 'log2':
            num='math.log2('
            new_num+='('

        self.result.set(new_num)
        temp=self.all_press_lists
        temp+=num
        self.all_press_lists=temp

    #按下AC
    def press_ac(self,sign):
        self.all_press_lists.clear()
        self.record.set("")
        self.result.set(0)

    


    #按下back
    def press_back(self, sign):
        num=self.result.get()
        a = num[0:-1]
        
        self.result.set(a)
        
        
        num=self.all_press_lists
        if len(num)>5 and num[-2] == '.' and num[-3] == 'h' and num[-4] == 't':
            a = num[:-6]
            self.all_press_lists=a
        elif len(num)>3 and num[-1] == 'i' and num[-2] == 'p':
            a = num[:-7]
            self.all_press_lists=a
        elif len(num)>1 and num[-1] == '*' and num[-2] == '*':
            a = num[:-2]
            self.all_press_lists=a
        elif len(num)>8 and num[-1] == 't' and num[-2] == 'r':
            a = num[:-9]
            self.all_press_lists=a
        elif len(num)>8 and num[-1] == '1' and num[-2] =='g' and num[-3] == 'o' and num[-4] == 'l':
            a = num[:-9]
            self.all_press_lists=a
        elif len(num)>7 and num[-1] == 'g' and num[-2] =='o' and num[-3] == 'l' and num[-4] == '.':
            a = num[:-8]
            self.all_press_lists=a
        elif len(num)>6 and num[-1] == 'o' and num[-2] =='l' and num[-3] == '.' and num[-4] == 'h':
            a = num[:-7]
            self.all_press_lists=a
        else:
            a = num[0:-1]
            self.all_press_lists=a


    # 获取运算结果
    def press_equal(self):
        
        temp=self.result.get()
        compute_str = ''.join(self.all_press_lists)
        try:
            calculate_result = eval(compute_str)
        except:
            calculate_result = 'error'
        self.result.set(calculate_result)  # 显示结果
        self.record.set(temp + "=")  # 显示运算过程
        self.all_press_lists.clear()  # 清空列表内容
        self.is_press_compute = True




class Calculator:
    def __init__(self):
        self.root = tkinter.Tk()
        self.all_press_lists = []  # 保存运算数字和符号的列表
        self.is_press_compute = False  # 判断是否按下运算按钮,默认没有按下
        self.result = tkinter.StringVar()  # 显示输入的数字及结果
        self.record = tkinter.StringVar()  # 显示计算过程

    def main(self):
        self.root.minsize(375, 620)  # 显示框的最小长宽
        self.root.title('标准计算器')  # 标题

        btn_w, btn_h = 93.75, 84  #按钮宽和高
        my_font = tkinter.font.Font(family='微软雅黑', size=20)  # 设置字体
        self.result.set(0)
        self.record.set('')
        input_bg, btn_fg, btn_bg = "#f8f8f8", "#000011", "#ffffff"  # 设定颜色
        # displayscreen
        label = tkinter.Label(self.root, font=my_font, bg=input_bg, bd='9', fg=btn_fg, anchor='se',
                              textvariable=self.record)
        label.place(width=375, height=120)
        label2 = tkinter.Label(self.root, font=my_font, bg=input_bg, bd='9', fg=btn_fg, anchor='se',
                               textvariable=self.result)
        label2.place(y=120, width=375, height=80)







        btn_change=tkinter.Button(self.root, text='切 换', font=tkinter.font.Font(family='微软雅黑', size=20), bg=btn_bg, fg="#49506c", bd=0,
                                command=lambda: self.press_change())
        btn_change.place(x=btn_w * 0, y=0, width=btn_w, height=btn_h/2)
        # 第一行
        btn_ac = tkinter.Button(self.root, text='c', font=my_font, bg="#cdeeef", fg=btn_fg, bd=0,
                                command=lambda: self.press_ac('AC'))
        btn_ac.place(x=btn_w * 0, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_back = tkinter.Button(self.root, text='Back', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                  command=lambda: self.press_back('b'))
        btn_back.place(x=btn_w * 1, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_per = tkinter.Button(self.root, text='%', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('%'))
        btn_per.place(x=btn_w * 2, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_divi = tkinter.Button(self.root, text='÷', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                  command=lambda: self.press_num('/'))
        btn_divi.place(x=btn_w * 3, y=200 + btn_h * 0, width=btn_w, height=btn_h)

        # 第二行
        btn7 = tkinter.Button(self.root, text='7', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('7'))
        btn7.place(x=btn_w * 0, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn8 = tkinter.Button(self.root, text='8', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('8'))
        btn8.place(x=btn_w * 1, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn9 = tkinter.Button(self.root, text='9', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('9'))
        btn9.place(x=btn_w * 2, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_mul = tkinter.Button(self.root, text='×', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('*'))
        btn_mul.place(x=btn_w * 3, y=200 + btn_h * 1, width=btn_w, height=btn_h)

        # 第三行
        btn4 = tkinter.Button(self.root, text='4', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('4'))
        btn4.place(x=btn_w * 0, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn5 = tkinter.Button(self.root, text='5', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('5'))
        btn5.place(x=btn_w * 1, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn6 = tkinter.Button(self.root, text='6', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('6'))
        btn6.place(x=btn_w * 2, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn_sub = tkinter.Button(self.root, text='-', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('-'))
        btn_sub.place(x=btn_w * 3, y=200 + btn_h * 2, width=btn_w, height=btn_h)

        # 第四行
        btn1 = tkinter.Button(self.root, text='1', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('1'))
        btn1.place(x=btn_w * 0, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn2 = tkinter.Button(self.root, text='2', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('2'))
        btn2.place(x=btn_w * 1, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn3 = tkinter.Button(self.root, text='3', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('3'))
        btn3.place(x=btn_w * 2, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn_add = tkinter.Button(self.root, text='+', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                 command=lambda: self.press_num('+'))
        btn_add.place(x=btn_w * 3, y=200 + btn_h * 3, width=btn_w, height=btn_h)

        # 第五行
        btn_pai=tkinter.Button(self.root, text='π', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('π'))
        btn_pai.place(x=btn_w * 0, y=200 + btn_h * 4, width=btn_w , height=btn_h)
        btn0 = tkinter.Button(self.root, text='0', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                              command=lambda: self.press_num('0'))
        btn0.place(x=btn_w * 1, y=200 + btn_h * 4, width=btn_w , height=btn_h)
        btn_point = tkinter.Button(self.root, text='.', font=my_font, bg=btn_bg, fg=btn_fg, bd=0,
                                   command=lambda: self.press_num('.'))
        btn_point.place(x=btn_w * 2, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        btn_equ = tkinter.Button(self.root, text='=', bg='#00bbbe', font=my_font, fg=btn_fg, bd=0,
                                 command=lambda: self.press_equal())
        btn_equ.place(x=btn_w * 3, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        self.root.mainloop()



    def press_change(self):
        self.root.destroy()
        my_calculator = scienceCalculator()
        my_calculator.main()


       # 按下数字
    def press_num(self, num):
        if self.is_press_compute is True:  # 如果判断等号按键被按下
            self.record.set("")
            self.result.set(0)  # 清空self.result
            self.is_press_compute = False
        
        # 判断界面的数字是否为0
        old_num = self.result.get()
        new_num=[]
        if old_num == '0' and num != '.':
            new_num=num
            
        else:
            new_num = old_num+num
            
        
        #判断特殊的符号
        if num == '^':
            num='**'
        elif num == '√':
            num='math.sqrt('
            new_num+='('
        elif num == 'sin':
            num='math.sin('
            new_num+='('
        elif num == 'cos':
            num='math.cos('
            new_num+='('
        elif num == 'tan':
            num='math.tan('
            new_num+='('
        elif num == 'lg':
            num='math.log10('
            new_num+='('
        elif num == 'ln':
            num='math.log('
            new_num+='('
        elif num == 'π':
            num='math.pi'
        elif num == 'asin':
            num='math.asin('
            new_num+='('
        elif num == 'acos':
            num='math.acos('
            new_num+='('
        elif num == 'atan':
            num='math.atan('
            new_num+='('
        elif num == 'e':
            num='math.e'
        elif num == 'log2':
            num='math.log2('
            new_num+='('
        


        self.result.set(new_num)
        temp=self.all_press_lists
        temp+=num
        self.all_press_lists=temp

    #按下AC
    def press_ac(self,sign):
        self.all_press_lists.clear()
        self.record.set("")
        self.result.set(0)




    # 按下back
    def press_back(self, sign):
        num=self.result.get()
        a = num[0:-1]
        
        self.result.set(a)
        
        
        num=self.all_press_lists
        if len(num)>5 and num[-2] == '.' and num[-3] == 'h' and num[-4] == 't':
            a = num[:-6]
            self.all_press_lists=a
        elif len(num)>3 and num[-1] == 'i' and num[-2] == 'p':
            a = num[:-7]
            self.all_press_lists=a
        elif len(num)>1 and num[-1] == '*' and num[-2] == '*':
            a = num[:-2]
            self.all_press_lists=a
        elif len(num)>8 and num[-1] == 't' and num[-2] == 'r':
            a = num[:-9]
            self.all_press_lists=a
        elif len(num)>8 and num[-1] == '1' and num[-2] =='g' and num[-3] == 'o' and num[-4] == 'l':
            a = num[:-9]
            self.all_press_lists=a
        elif len(num)>7 and num[-1] == 'g' and num[-2] =='o' and num[-3] == 'l' and num[-4] == '.':
            a = num[:-8]
            self.all_press_lists=a
        elif len(num)>6 and num[-1] == 'o' and num[-2] =='l' and num[-3] == '.' and num[-4] == 'h':
            a = num[:-7]
            self.all_press_lists=a
        else:
            a = num[0:-1]
            self.all_press_lists=a

    # 获取运算结果
    def press_equal(self):
        
        temp=self.result.get()
        compute_str = ''.join(self.all_press_lists)
        try:
            calculate_result = eval(compute_str)
        except:
            calculate_result = 'error'
        self.result.set(calculate_result)  # 显示结果
        self.record.set(temp + "=")  # 显示运算过程
        self.all_press_lists.clear()  # 清空列表内容
        self.is_press_compute = True

if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.main()