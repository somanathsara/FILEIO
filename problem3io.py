"""Wrote a programm to genrate multiplication table from 2 to 20 & write it to the different files.place the files 
in a folder for a 13 - year old"""
# import os
# os.makedirs("tables",exist_ok=True)
def generate_table(i):
    table = ""
    for j in range(1,11):
        table += f"{i} * {j} = {i*j}\n"
    with open(f"tables/table_{i}.txt","w") as file:
        file.write(table)
for i in range(1,21):
    generate_table(i)    