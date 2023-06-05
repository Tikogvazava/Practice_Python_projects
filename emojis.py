message= input(">")

words= message.split(' ')

emojis ={
    ":)": "smileyface",   #you can insert emojies instead of these words"
    ":(": "sadface"
    }
print(words)

output =""
for i in words:
   output+= emojis.get(i, i)+" "

print(output)
    
