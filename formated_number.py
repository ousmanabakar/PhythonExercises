def print_formatted(number):
    for i in range(1,number + 1):
        print("",i,oct(i).replace("0o"," "),hex(i).replace("0x"," "),bin(i).replace("0b"," "))


n = int(input())
print_formatted(n)
