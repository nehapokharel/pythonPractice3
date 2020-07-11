import csv

class Student:
    

    def course_list(self,course_detail):
        for k, v in course_detail.items():
            if k == 'course_name':
                print(v)



obj = Student()
course_info = csv.DictReader(open("course_of_study.csv"))

print('**************************')
print("Welcome to IT Academy!!")
print('**************************')
print(' ')
print("We provide following courses: ")
for courses in course_info:
    obj.course_list(courses)
print(' ')
print("Do you want to know more about these courses?")
print(' ')