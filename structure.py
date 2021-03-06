"""
Program's name : Hong-Rean
Program : To make classroom and exam room
Author : Mr.Atiwat Vorasaksirikul and Mr.Kittituch Pavaranchanakul
Language : Python 2.7.8
GUI : Tkinter from Python
"""
import random
import tkMessageBox
from Tkinter import *
class App:
    def __init__(self, master):
        """Make two buttons at first when you open a program"""
        Label(master, text = "Welcome to 'Hong-Rean'", fg = "blue", font = ("Helvetica", 28, "bold")).grid(padx = 15, pady = 15)
        Label(master, text = "Instruction:", font = ("Helvetica", 16, "bold")).grid(padx = 10, pady = 1)
        Label(master, text = "Select your choice to select your class", font = ("Helvetica", 16)).grid(padx = 5, pady = 2)
        description = "If you choose 'Class-room' your class-room will be selected by grade.\n If you choose 'Exam-room' your exam-room will be selected randomly."
        Label(master, text = description).grid(padx = 5, pady = 5)
        Button(master, text = "Let's start!", command = self.hongrean).grid(padx = 15, pady = 15)

    def hongrean(self):
        """Make two buttons at first when you open a program"""
        self.first = Toplevel()
        Label(self.first, text = "Choose it!", font = ("Helvetica", 18, "bold")).grid(padx = 10, pady = 10, column = 1)
        #make ('Class Room')'s button
        class_room = Button(self.first, text = "Class Room", command = self.class_arrange).grid(padx = 20, pady = 10, row = 1, column = 0)
        #make ('Exam Room')'s button
        exam_room = Button(self.first, text = "Exam Room", command = self.exam_arrange).grid(padx = 20, pady = 10, row = 1, column = 2)

    def class_arrange(self):
        """This is about when you press classroom's button"""
        self.top = Toplevel() #set new window

        self.num_of_stu = IntVar() #input number of student(int value)

        Label(self.top, text = "Number of \nStudent :").grid(padx = 5, pady = 5, row = 0, column = 0)
        Entry(self.top, textvariable = self.num_of_stu, width = 5).grid(padx = 5, pady = 5, row = 0, column = 1) #Empty for input

        self.button = Button(self.top, text = "Submit", command = self.slot)
        self.button.grid(padx = 5, pady = 5, row = 0, column = 2)

    def exam_arrange(self):
        """This is about when you press exam's button"""
        self.windows = Toplevel() #set new window
        self.windows.maxsize(width = 350, height = 418) #size
        self.num_of_stu = StringVar(value = 1)
        self.width = StringVar(value = 1)
        self.height = StringVar(value = 1)
        Label(self.windows, text = "Number of Student: ").grid(padx = 5, pady = 5, row = 0, column = 0)
        Entry(self.windows, textvariable = self.num_of_stu, width = 5).grid(padx = 5, pady = 5, row = 0, column = 1)

        Label(self.windows, text = "Room Size\n'width x height'").grid(padx = 5, pady = 5, row = 1, column = 0)
        Entry(self.windows, textvariable = self.width, width = 5).grid(padx = 5, pady = 5, row = 1, column = 1)
        Label(self.windows, text = "x").grid(padx=5, pady=5, row=1, column=2)
        Entry(self.windows, textvariable = self.height, width = 5).grid(padx = 5, pady = 5, row = 1, column = 3)
        Button(self.windows, text = "Proceed", command = self.exam_selection).grid(padx = 5, pady = 5, row = 2, column = 3)

        self.text = Text(self.windows, width = 40, height = 10, wrap = NONE)
        self.text.grid(padx = 3, pady = 3, row = 3, column = 0, columnspan = 4)
    def slot(self):
        """in Classroom button"""
        try:
            int(self.num_of_stu.get())
            self.num = []
            self.grade = []
            Label(self.top, text = " ").grid(padx = 10, pady = 10, row = 1, column = 0)
            Label(self.top, text ="No.", width = 5).grid(padx = 10, pady = 10, row = 1, column = 1)
            proceed = Button(self.top, text = "Proceed", command = self.classroom_selection)
            Label(self.top, text = "Grade", width = 5).grid(padx = 10, pady = 10, row = 1, column = 2)
            for i in xrange(int(self.num_of_stu.get())):
                self.num.append("No" + str(i))
                self.grade.append("Grade" + str(i))

            for j in xrange(len(self.num)):
                self.num[j] = StringVar(value = j + 1)
                self.grade[j] = StringVar(value = 0.0)

                if j > 9:
                    Label(self.top, text = j + 1, width = 5).grid(padx = 10, pady = 5, row = 2 + j % 10, column = 2 + (3 * (j / 10) - 2))
                    Entry(self.top, textvariable = self.num[j], width = 5).grid(padx = 10, pady = 5, row = 2 + j % 10, column = 3 + (3 * (j / 10) - 2))
                    Entry(self.top, textvariable = self.grade[j], width = 5).grid(padx = 10, pady = 5, row = 2 + j % 10, column = 4 + (3 * (j / 10) - 2))
                    proceed.grid(row = len(self.num) + 2, column = 4 + (3 * (j/10) - 2), padx = 20, pady = 15)
                else:
                    Label(self.top, text = j + 1, width = 5).grid(padx = 10, pady = 5, row = 2 + j, column = 0)
                    Entry(self.top, textvariable = self.num[j], width = 5).grid(padx = 10, pady = 5, row = 2 + j, column = 1)
                    Entry(self.top, textvariable = self.grade[j], width = 5).grid(padx = 10, pady = 5, row = 2 + j, column = 2)
                    proceed.grid(row = len(self.num) + 2, column = 2, padx = 20, pady = 15)

            self.button.config(state = "disabled")
        except:
            tkMessageBox.showerror(title = "Input Error", message = "Input must be number")

    def classroom_selection(self):
        """classroom befor process about to give grade and number of each student"""
        try:
            for i in xrange(len(self.num)):
                int(self.num[i].get())
                float(self.grade[i].get())
            self.topend = Toplevel()
            new_num = [int(i.get()) for i in self.num]
            new_grade = [float(j.get()) for j in self.grade]
            select_dict = dict()
            output_list = list()
            printer = "RESULT: \n"
            for i in xrange(len(new_num)):
                select_dict[new_num[i]] = new_grade[i]

            for i in xrange(len(new_num) / 2):
                for i in select_dict:
                    if select_dict[i] == max(select_dict.values()):
                        stu_1 = i
                        select_dict.pop(i)
                        break
                for i in select_dict:
                    if select_dict[i] == min(select_dict.values()):
                        stu_2 = i
                        select_dict.pop(i)
                        break
                output_list.append([stu_1, stu_2])
            if select_dict != {}:
                num, grade = select_dict.popitem()
                if len(output_list) == 0:
                    output_list.append([num])
                else:
                    output_list[-1].append(num)
            for i in output_list:
                printer += str(i) + "\n"
            self.text = Text(self.topend, width = 40, height = 10, wrap = NONE)
            self.text.grid(padx = 3, pady = 3, row = 3, column = 0, columnspan = 4)
            self.text.delete(0.0, END)
            self.text.insert(1.0, printer)
        except:
            tkMessageBox.showerror(title = "Input Error", message = "Input must be number")
    def exam_selection(self):
        """when you go exam button this is process in it"""
        try:
            num_stu = int(self.num_of_stu.get())
            data = list()
            width = int(self.width.get())
            height = int(self.height.get())
            if width * height < num_stu:
                return None
            else:
                printer = "RESULT: \n"
                counter = 0
                for i in xrange(num_stu):
                    data.append(i + 1)
                for i in xrange(height):
                    if counter > num_stu - 1:
                        break
                    for j in xrange(width):
                        if counter > num_stu - 1:
                            break
                        num = random.choice(data)
                        printer += [str(num), "0" + str(num)][len(str(num)) == 1] + [" ", "\n"][j == width - 1]
                        data.remove(num)
                        counter += 1
                self.text.delete(0.0, END)
                self.text.insert(0.0, printer)
        except:
            tkMessageBox.showerror(title = "Input error", message = "Input must be number")

def main(root):
    """main function of program"""
    app = App(root)
    root.title("Hong-Rean")
    root.mainloop()
    root.destroy()
main(Tk())
