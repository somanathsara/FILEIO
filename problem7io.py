"""Write a programm to find out the line number where python is present from problem 6"""
with open("log.txt","r")  as file:
    data = file.readlines()
line_no = 1
for  line in data:
    if("python" in line):
        print("Python is present is line-",line_no)
        break
    else:
        print("python is not present.")
    line_no += 1
    