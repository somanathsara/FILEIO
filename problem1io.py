with open("poem.txt","r") as file:
    data = file.read()
if("Twinkle" in data):
    print("The word Twinkle  is present.")
else:
    print("The word is not present")