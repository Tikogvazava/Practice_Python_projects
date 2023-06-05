def emoji_converter(message):  #here message is a parameter = sentence
   words= message.split(' ')

   emojis ={
       ":)": "smilyface",   #you can insert emojies instead of these words"
       ":(": "sadface"
   }

   output =""
   for word in words:
      output+= emojis.get(word, word)+" "
   return output

message=input(">")
print(emoji_converter(message))
