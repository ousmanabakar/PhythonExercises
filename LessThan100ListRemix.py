#Given a list of numbers, return True if the sum of the list is less than 100; otherwise return False.

def list_less_than_100(lst):
	total=0
	for i in lst:
		total +=i
	total
	if total <100:
		return True
	else:
		return False
