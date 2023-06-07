
from proj07 import get_min

data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], 
[('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]]
cities = ['lansing_small', 'chicago_small']
print("data:",data)
print("cities:",cities)
col = 2
print("column #:",col)
instructor = [('lansing_small', 18.0), ('chicago_small', 29.0)]
print("Instructor:")
print(instructor)
student = get_min(col,data,cities)
print("Student:")
print(student)
assert student == instructor

print("\n"+"-"*20)
col = 5
print("column #:",col)
instructor = [('lansing_small', 0.4), ('chicago_small', 0.1)]
print("Instructor:")
print(instructor)
student = get_min(col,data,cities)
print("Student:")
print(student)
assert student == instructor

