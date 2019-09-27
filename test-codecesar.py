alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
word = "nez"
offset = 1
new_word = ""

for i in range (len(word)):
    letter = word[i]
    position_in_alphabet = alphabet.index(letter)
    new_position_alphabet = (position_in_alphabet + offset) % len(alphabet)
    new_letter = alphabet[new_position_alphabet]
    new_word += new_letter
print (new_word)

