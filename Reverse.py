# Tech Tinkerers 1/31/2014
# Reverse a string

in_string = raw_input("Enter a string: ")
new_string = ""
for index_in in range(len(in_string)-1,-1,-1):
   new_string += in_string[index_in]
print new_string
