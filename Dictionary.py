phone=input("Phone: ")

digits_as_string ={
    "1": "One",
 "2": "Two",
 "3": "Three",
 "4": "Four"
 }

output= ""
for i in phone:
    output+=digits_as_string.get(i, "!")+" "


print(output)


#get function grabs i from phone and connects it to the value that we have given in dictionary. "output" creates a variable where we use get "method" to get i from input numbers. if the number isn't given in the dictionary ! is given in the print output. 
