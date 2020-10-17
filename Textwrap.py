import textwrap

def wrap(string, max_width):

    # Wrap this text. 
    wrapper = textwrap.TextWrapper(max_width)

    string = wrapper.fill(text=string) 
    
    return string


string = input("Enter your string: ")
max_width = int(input("Enter max width: "))

result = wrap(string, max_width)
print(result)
