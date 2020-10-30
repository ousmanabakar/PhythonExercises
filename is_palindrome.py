def is_palindrome(input_string):
	
	new_string = ""
	reverse_string = ""

	for i in input_string:

		if len(input_string)>0:
			new_string =input_string.replace(" ","").lower()
			reverse_string=input_string[::-1].replace(" ","").lower()

	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
