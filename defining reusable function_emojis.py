def emoji_converter(message):  #here message is a parameter = sentence
   words= message.split(' ')

   emojis ={
       ":)": "dzunkaldzunkal",   #you can insert emojies instead of these words"
       ":(": "tanklitunkli"
   }

   output =""
   for word in words:
      output+= emojis.get(word, word)+" "
   return output

message=input(">")
print(emoji_converter(message))
