def average(array):
    # your code goes here
    set1=set(array)
    avr=0
    for i in set1:
        avr +=i

    return avr / len(set1)


n = int(input())  # e.g. n = 10
arr = list(map(int, input().split())) #arr= [1,2,2,3,.....] len=10
result = average(arr)
print(result)
