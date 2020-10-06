import time

def square(numbers):
    
    result = []
    
    start_time = time.time()
    
    for num in numbers:
        
        result.append(num ** 2)
        
    end_time = time.time()
    
    print("This func1 takes" + str(end_time - start_time) +" seconds")
        
    return result


def cube(numbers):
    
    result = []
    
    start_time = time.time()
    
    for num in numbers:
        
        result.append(num ** 3)
        
    end_time = time.time()
    
    print("This func2 takes" + str(end_time - start_time) +" seconds")
        
    return result

square(range(1001))
cube(range(5000))
