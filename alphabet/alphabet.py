def func(string):
	char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	split_string = string.split()
	i = 0
	x = ""

	# get letters
	string = string.lower()
	for s in string:
		if s in char:
		    string_index_in_char = char.index(s) + 1
		else:
		    string_index_in_char = "^"
		x += str(string_index_in_char)
		split_any_char_not_letters = x.split("^")
	# convert string into interger in list	
	for i in range(0, len(split_any_char_not_letters)): 
	    split_any_char_not_letters[i] = int(split_any_char_not_letters[i])		
	convert_to_int = split_any_char_not_letters	

	# (split_string, convert_to_int) comparison
	n = convert_to_int.index(max(convert_to_int))
	my_string = split_string[n]
	print("%s -> %s" %(string, my_string.lower()))
		

func("man i need a taxi up to ubud")
func("Hello wOrld")
func("what time are we climbing up to the volcano")
func("take me to semynak")
func("we exchanged the money on the dark")