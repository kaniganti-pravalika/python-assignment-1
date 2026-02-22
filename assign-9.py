#Capitalize First Letter of Each Word

sentence = input("Enter a sentence: ")

result = ""
new_word = True

for ch in sentence:
    if ch == " ":
        result += ch
        new_word = True
    elif new_word:
        result += ch.upper()
        new_word = False
    else:
        result += ch

print("Capitalized Sentence:", result)
