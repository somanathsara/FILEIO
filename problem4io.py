"""A file contain the word donkey multiple times
you need to write a program which replace donkey by ##### by updating the same file"""

word = "Donkey"
with open("donkey_file.txt","r") as file:
    data = file.read()
data = data.replace(word,"######")
# print(data)
with open("donkey_file.txt","w") as file2:
    file2.write(data)