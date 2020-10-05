def add(a,b):
    return a+b

def subs(a,b):
    return a-b

def divition(a,b):
    return a/b

def mult(a,b):
    return a * b


def main_function(func1,func2,func3,func4,operation):
    if operation == "add":
        print(func1(4,7))
        
    elif operation == "subs":
        print(func2(2,10))
        
    elif operation == "divition":
        print(func3(5,3))
        
    elif operation == "mult":
        print(func4(5,7))


main_function(add,subs,divition,mult,"add")
#result = 11

main_function(add,subs,divition,mult,"subs")
#result = -8

main_function(add,subs,divition,mult,"divition")
#result = 1.666666666

main_function(add,subs,divition,mult,"mult")
#result = 35
