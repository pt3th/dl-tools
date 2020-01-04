#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:57:16 2020

@author: q
"""

#简单的图形界面GUI（Graphical User Interface）
import tkinter as tk
import tkinter.messagebox as messagebox
import os
import numpy as np
class Application(tk.Frame):   #从Frame派生出Application类，它是所有widget的父容器
    def __init__(self,para_list,choice_list,exe_file,output_dir, master = None):#master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        tk.Frame.__init__(self,master)
        self.grid()#将widget加入到父容器中并实现布局
        self.para_list = para_list
        self.choice_list = choice_list
        self.len = len(para_list)
        self.str1 = 'min'
        self.str2 = 'max'
        self.str3 = '_rand_num'
        self.str4 = 'in'
        self.str5 = '_step'
        self.exe_file =exe_file
        self.createWidgets()

    def createWidgets(self):
        print(self.len)
        self.trainfile = tk.Label(self,text = 'python file')
        self.trainfile.grid()
        self.trainfilein = tk.Entry(self)
        self.trainfilein.grid()

        for i in range(self.len):
            para = self.para_list[i]
            mode = self.choice_list[i]
            prepare_list = locals()
            if mode == 'fixed':
                setattr(self,para,tk.Label(self,text=para))
                para_text = getattr(self,para)
                para_text.grid()
                setattr(self,para+'in',tk.Entry(self,text=para+'in'))
                para_entry = getattr(self,para+'in')
                para_entry.grid()                
            elif mode =='random':
                str1 = self.str1
                str2 = self.str2
                str3 = self.str3
                str4 = self.str4
                #min
                setattr(self,para+str1,tk.Label(self,text=para+str1))
                para_text = getattr(self,para+str1)
                para_text.grid()
                setattr(self,para+str1+str4,tk.Entry(self,text=para+str1+str4))
                para_entry = getattr(self,para+str1+str4)
                para_entry.grid()
                #max
                setattr(self,para+str2,tk.Label(self,text=para+str2))
                para_text = getattr(self,para+str2)
                para_text.grid()
                setattr(self,para+str2+str4,tk.Entry(self,text=para+str2+str4))
                para_entry = getattr(self,para+str2+str4)
                para_entry.grid()
                #random number
                setattr(self,para+str3,tk.Label(self,text=para+str3))
                para_text = getattr(self,para+str3)
                para_text.grid()
                setattr(self,para+str3+str4,tk.Entry(self,text=para+str3+str4))
                para_entry = getattr(self,para+str3+str4)
                para_entry.grid()                
            elif mode == 'step':
                str1 = self.str1
                str2 = self.str2
                str3 = self.str5
                str4 = self.str4
                #min
                setattr(self,para+str1,tk.Label(self,text=para+str1))
                para_text = getattr(self,para+str1)
                para_text.grid()
                setattr(self,para+str1+str4,tk.Entry(self,text=para+str1+str4))
                para_entry = getattr(self,para+str1+str4)
                para_entry.grid()
                #max
                setattr(self,para+str2,tk.Label(self,text=para+str2))
                para_text = getattr(self,para+str2)
                para_text.grid()
                setattr(self,para+str2+str4,tk.Entry(self,text=para+str2+str4))
                para_entry = getattr(self,para+str2+str4)
                para_entry.grid()
                #random number
                setattr(self,para+str3,tk.Label(self,text=para+str3))
                para_text = getattr(self,para+str3)
                para_text.grid()
                setattr(self,para+str3+str4,tk.Entry(self,text=para+str3+str4))
                para_entry = getattr(self,para+str3+str4)
                para_entry.grid()  
            else:
                print("choice error! Supported choice: 'fixed','randome','step'")
        self.nameButton = tk.Button(self,text = 'generate',command = self.generate)#generate file
        self.nameButton.grid()
 
    def generate(self):
        create_var = locals()
        para_list = self.para_list
        choice_list = self.choice_list
        for i in range(self.len):
            para = para_list[i]
            mode = choice_list[i]
            create_var[para] = []
            if mode == 'fixed':
                class_var = getattr(self,para+self.str4)
                create_var[para_list[i]].append(float(class_var.get()))
            elif mode == 'random':
                class_var_min = getattr(self,para+self.str1+self.str4)
                minval = float(class_var_min.get())
                class_var_max = getattr(self,para+self.str2+self.str4)
                maxval = float(class_var_max.get())
                class_var_num = getattr(self,para+self.str3+self.str4)
                num = int(class_var_num.get())
                arr = (maxval-minval)*np.random.rand(num) + minval
                arr = np.round(arr,3)
                create_var[para]=list(arr)
            elif mode == 'step':
                class_var_min = getattr(self,para+self.str1+self.str4)
                minval = float(class_var_min.get())
                class_var_max = getattr(self,para+self.str2+self.str4)
                maxval = float(class_var_max.get())
                class_var_step = getattr(self,para+self.str5+self.str4)
                step = float(class_var_step.get())
                arr = np.arange(minval,maxval,step)
                arr = np.round(arr,3)
                create_var[para]= list(arr)
            else:
                print("error!")
        trainfile = self.trainfilein.get()
        f = open(self.exe_file,'w')
        total_num = 1
        para_len = []
        for i in range(self.len):
            total_num = total_num*len(create_var[para_list[i]])
            para_len.append(len(create_var[para_list[i]]))
        for i in range(total_num):
            s = 'python '+trainfile+' '
            for j in range(self.len):
                s = s + '--'+para_list[j] + ' '+str(create_var[para_list[j]][i%para_len[j]])+' ' 
            s = s + '--output_dir '+output_dir + str(i)
            f.write(s+'\n')
        f.close()
        command = 'chmod +x '+self.exe_file 
        os.system(command)
        messagebox.showinfo('Message','Done')#显示输出
#parameter list
para_list = ['cf','pf','rf']

#choice_list
#fixed only one value
#random uniform sampling
#step linear sampling
choice_list = ['fixed','random','step']

#
bash_file = 'run_test'

#
output_dir = 'A->C'
app = Application(para_list,choice_list,bash_file,output_dir)
app.master.title("Fine Tuning Master")#窗口标题
app.master.geometry("500x400")
app.mainloop()#主消息循环