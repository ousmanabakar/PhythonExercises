def main_func(operation_name):
    
    def addition(*args):
        result1 = 0
        for i in args:
            result1 += i
        return result1
    
    def mult(*args):
        result2 = 1
        for i in args:
            result2 *= i
        return result2
    
    if operation_name == "addition":
        return addition
    else:
        return mult
    



func1 = main_func("addition")

func1(1,2,3,4,5)

func2 = main_func("mult")

func2(1,2,3,4,5)
