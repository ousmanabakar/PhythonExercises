def split_and_join(line):

    # write your code here
    line= line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input("Enter a string:")
    result = split_and_join(line)
    print(result)
