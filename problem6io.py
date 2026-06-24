"""write a programm to mine a log file & findout whether it contains pyhton or not."""
with open("log.txt","w") as file:
    file.write("Python is modern programming language used bby AI")
with open("log.txt","r") as file:
    data = file.read()
if("Python" in data):
    print("Python is present.")
else:
    print("Python is not present")