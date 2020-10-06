import time

def time_calculate(func):
    def wrapper(numbers):
        
        start_time = time.time()
        result = func(numbers)
        
        end_time = time.time()
        
        print(func.__name__ +" takes " + str(end_time - start_time) +" seconds")
        return result
    
    return wrapper
      
@time_calculate   
def square_func(numbers):
    
    result = []
    
    for num in numbers:        
        result.append(num ** 2)          
    return result


@time_calculate 
def cube_func(numbers):
    
    result = []
    for num in numbers:      
        result.append(num ** 3)
    return result

square_func(range(6000))
cube_func(range(4000))
