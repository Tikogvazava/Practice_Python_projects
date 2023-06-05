secret_number=8
guess_count=0
guess_limit=4

while guess_count<guess_limit:
    guess_number=int(input("guess the number: "))
    guess_count+=1
    if guess_number==secret_number:
        print ("Good job! you guessed it right.")
        break
else: print ("You are wrong! Try again.")

