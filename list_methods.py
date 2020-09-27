if __name__ == '__main__':
    N = int(input())
    arr=[]
    arr.insert(0,5)
    arr.insert(1,10)
    arr.insert(0,6)
    print(list(arr))
    arr.remove(6)
    arr.append(9)
    arr.append(1)
    arr.sort()
    print(list(arr))
    arr.pop()
    arr.reverse()
    print(list(arr))


    
    
