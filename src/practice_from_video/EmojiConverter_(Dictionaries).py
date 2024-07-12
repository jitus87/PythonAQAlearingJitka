# converts symbols to emoji pictures

message = input("> ")
words = message.split(' ') #when space is found, it' s used as separator and splits message into separate words, makes a list
emojis = {
    ":)": "😊",  # press WIN+. or WIN+;
    ":(": "😒",
}

output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)
