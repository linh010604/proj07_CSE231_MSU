from proj07 import get_data_in_range
master_list = [
[('5/2/1999', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
('3/1/2000', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
('1/1/2000', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
('12/31/2001', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0),
 ('3/6/2002', 31.0, 34.0, 28.0, 0.0, 0.1, None)
], 
[('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), 
('11/20/2003', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)
]
]
start_date = '1/1/2000'
end_date = '12/31/2001'
instructor = [[('3/1/2000', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
('1/1/2000', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
('12/31/2001', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)
], 
[('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None)
]
]
print("Instructor:")
print(instructor)
student = get_data_in_range(master_list,start_date,end_date)
print("Student:")
print(student)
assert student == instructor

print("\n"+"-"*20)
start_date = '1/1/1900'
end_date = '12/31/2025'
instructor = [
[('5/2/1999', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
('3/1/2000', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
('1/1/2000', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
('12/31/2001', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0),
 ('3/6/2002', 31.0, 34.0, 28.0, 0.0, 0.1, None)
], 
[('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), 
('11/20/2003', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)
]
]
print("Instructor:")
print(instructor)
student = get_data_in_range(master_list,start_date,end_date)
print("Student:")
print(student)
assert student == instructor