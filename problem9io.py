"""Write a programm to find out whether a file is identical to content of another file or not."""
with open("poem.txt","r")as file:
    data1 = file.read()
with open("poem_copy.txt","r")as file:
    data2 = file.read()
if(data1 == data2):
    print("These two files are identical.")
else:
    print("These two files are not identical.")