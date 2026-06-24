"""write a programm to make a copy of a text file this.txt"""
with open("poem.txt","r") as file:
    content = file.read()
with open("poem_copy.txt","w") as file:
    file.write(content)
