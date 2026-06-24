"""Repeat the problem 4 for a list such words  to be consored"""
list1 = ["Ram","Shyam","Gopal","Hari"]
with open("list_consoration.txt","r") as file:
    data = file.read()
for i in list1:
    data = data.replace(i,len(i)*"#")
#print(data)
with open("list_consoration.txt","w") as file:
    file.write(data)