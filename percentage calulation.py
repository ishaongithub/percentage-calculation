# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:49:31 2022

@author: ishar
"""

from tkinter import *
root=Tk()
root.title("Percentage Calculation")
root.geometry("500x500")



class grade3():
    def __init__(self,lang_arts,math):
        self.lang_arts=lang_arts
        self.math=math
    def percent(self):
        total_marks=self.lang_arts+self.math
        total_marks_100=total_marks*100
        grade_3_percent=total_marks_100/200
        label_3["text"]=str(grade_3_percent)
        
class grade5():
    def __init__(self,lang_arts,math,social):
        self.lang_arts=lang_arts
        self.math=math
        self.social=social
    def percent(self):
        total_marks=self.lang_arts+self.math+self.social
        total_marks_100=total_marks*100
        grade_5_percent=total_marks_100/300
        label_5["text"]=str(grade_5_percent)

class grade10():
    def __init__(self,lang_arts,math,social, foreign_lang):
        self.lang_arts=lang_arts
        self.math=math
        self.social=social
        self.foreign_lang=foreign_lang
    def percent(self):
        total_marks=self.lang_arts+self.math+self.social+self.foreign_lang
        total_marks_100=total_marks*100
        grade_10_percent=total_marks_100/400
        label_10["text"]=str(grade_10_percent)

object_3=grade3(30,40)
object_5=grade5(50,70,80)
object_10=grade10(60,90,87,97)
btn_3=Button(root, text="Grade 3", command=object_3.percent)
btn_3.pack(padx=20, pady=10)
label_3=Label(root)
label_3.pack()

btn_5=Button(root, text="Grade 5", command=object_5.percent)
btn_5.pack(padx=20, pady=10)
label_5=Label(root)
label_5.pack()

btn_10=Button(root, text="Grade 10", command=object_10.percent)
btn_10.pack(padx=20, pady=10)
label_10=Label(root)
label_10.pack()

root.mainloop()
    
        