try:                         #we tell program "hey try this code, but if you encounter ValueError instead of crashing the program print that. 
   age=int(input("Age: "))
   income=20000
   risk=income/age
   print(age)
except ZeroDivisionError:
   print("Age cannot be zero")
except ValueError:
   print("Invalid Value") 
