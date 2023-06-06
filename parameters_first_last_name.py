def greetings(first_name):  #first_name is a parameters which is a placeholder. we define a function for receiving an information 
   print(f"Hi {first_name}, hope you enjoyed your stay!")
   print("Please, visit us again")

print("start") 
greetings("Tiko")   #first_names here are actual piece of information- arguments. we supply arguments to these functions, where first_name is a parameter.
greetings("Anabel")
greetings("John")
greetings("Jennifer")
print("finish")



#with the last name 


def greetings(first_name, last_name):  
   print(f"Hi {first_name} {last_name}, hope you enjoyed your stay!")
   print("Please, visit us again")

print("start") 
greetings("Tiko", "Gvazava")   
greetings("Anabel", "Petrova")
greetings("John",  "Cena")
greetings("Jennifer", "Aniston")
print("finish")
