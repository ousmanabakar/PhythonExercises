"""
enter an int n and print it like this:
n =3
not like this:
1
2
3
but like this: 123 without space
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
