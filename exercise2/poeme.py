# class Poeme:
#     def __init__(self):
with open("poeme.txt", "r",encoding="utf-8") as file:
    content = file.read()
    lines = content.split("\n")
    #print(content)
    first_char = ""
    for line in lines:
         first_char += line[0]
         print(line[0])
    print(first_char)

#poeme = Poeme()