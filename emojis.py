message= input(">")

words= message.split(' ')

emojis ={
    ":)": "dzunkaldzunkal",   #you can insert emojies instead of these words"
    ":(": "tanklitunkli"
    }
print(words)

output =""
for i in words:
   output+= emojis.get(i, i)+" "

print(output)
    
