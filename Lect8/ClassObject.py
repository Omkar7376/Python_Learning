#1. create student class that takes name and marks of three students as argument in cunstructor and has a method to calculate the average marks. 

class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    def cal_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of ", self.name, " is ", sum/len(self.marks))
            

s1 = Student("Omkar", [99,86,76])
s1.cal_avg()