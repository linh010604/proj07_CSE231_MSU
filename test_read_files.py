from proj07 import read_files
fp1=open("lansing_small.csv",'r')
fp2=open("chicago_small.csv",'r')
cities_fp = [fp1,fp2]
print("opening lansing_small.csv,chicago_small.csv")
instructor = [
[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)
], 
[('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), 
('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)
]
]
print("Instructor:")
print(instructor)
student = read_files(cities_fp)
print("\nStudent:")
print(student)
assert student == instructor
print('\n'+'-'*20)
fp1=open("lansing_small.csv",'r')
cities_fp = [fp1]
print("opening lansing_small.csv")
instructor = [
[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)
]
]
print("Instructor:")
print(instructor)
student = read_files(cities_fp)
print("\nStudent:")
print(student)
assert student == instructor