with open("email.txt","r",encoding="utf-8") as file:
    for line in file:
        line = line[:-1]
        if  (line.endswith(".com") and line.find("@") !=-1):
            print(line)



