from Tkinter import *
class App:
    def __init__(self, master):
        class_room = Button(text="Class Room", command=self.class_arrange)
        exam_room = Button(text="Exam Room")

        class_room.grid(padx=10, pady=10, row=0, column=0)
        exam_room.grid(padx=10, pady=10, row=0, column=1)

    def class_arrange(self):
        self.top = Toplevel() #set new window
        
        self.num_of_stu = IntVar() #input number of student(int value)

        Label(self.top, text="Number of Student :").grid(padx=10, pady=10, row=0, column=0)
        Entry(self.top, textvariable=self.num_of_stu).grid(padx=10, pady=10, row=0, column=1) #Empty for input

        Button(self.top, text="Submit", command=self.slot).grid(padx=10, pady=10, row=0, column=2)

    def slot(self):
        self.num = []
        self.grade = []
        Label(self.top, text=" ").grid(padx=10, pady=10, row=1, column=0)
        Label(self.top, text="Student No.", width=10).grid(padx=10, pady=10, row=1, column=1)
        Label(self.top, text="Grade", width=10).grid(padx=10, pady=10, row=1, column=2)
        for i in xrange(self.num_of_stu.get()):
            self.num.append("No" + str(i))
            self.grade.append("Grade" + str(i))
            
        for j in xrange(len(self.num)):
            scrollbar = Scrollbar(self.top)
            self.num[j] = IntVar()
            self.grade[j] = IntVar()

            Label(self.top, text=j+1, width=5).grid(padx=10, pady=10, row=j+2, column=0)
            Entry(self.top, textvariable=self.num[j], width=10).grid(padx=10, pady=10, row=j+2, column=1)
            Entry(self.top, textvariable=self.grade[j], width=10).grid(padx=10, pady=10, row=j+2, column=2)
        proceed = Button(self.top, text="Proceed", command=self.selection)
        proceed.grid(row=len(self.num)+2, column=2, padx=10, pady=10)
        
    def selection(self):
        self.topend = Toplevel()
        new_num = [int(i.get()) for i in self.num]
        new_grade = [int(j.get()) for j in self.grade]

        Label(self.topend, text=new_num).grid(padx=10, pady=10, row=2, column=0)
        Label(self.topend, text=new_grade).grid(padx=10, pady=10, row=4, column=0)
          
        
root = Tk()
app = App(root)
root.mainloop()
