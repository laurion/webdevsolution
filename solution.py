# WebDev solution
def divide_by_two(i):
	return i/2
def add_one(i):
	return i+1
def multiply_by_five(i):
	return i*5
def subtract_three(i):
	return i-3
def add_two(i):
	return i+2
def multiply_by_three(i):
	return i*3

def apply_fcts(i, the_list):
	ret = []
	for f in the_list:
		try:
			ret.append(f(i))
		except:
			print "Not a defined function!"
	return ret

if __name__ == "__main__":
	try:
		i = int(raw_input("Please enter a number: "))
	except ValueError:
		print "That was not a valid number!"
	else:
		try:
			the_list = input("Please enter the list of functions: ")
			if(type(the_list) is not list):
				raise ValueError
		except ValueError:
			print "That was not a valid list of functions"
		else:
			print apply_fcts(i,the_list)
	print "\nThe tests:"
	print apply_fcts(4,[add_one, multiply_by_five])
	print apply_fcts(7,[subtract_three, add_two, multiply_by_three])

